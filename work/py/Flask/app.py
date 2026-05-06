from flask import Flask, render_template, request
from gpiozero import LED, Buzzer, DistanceSensor
from gpiozero import PWMOutputDevice
from RPLCD.i2c import CharLCD
import threading
import time

app = Flask(__name__)
buzzer = PWMOutputDevice(18)

# 1. 하드웨어 설정 (현빈님 현재 연결 상태)
led = LED(17)          # LED 17번 하나만 사용
#buzzer = Buzzer(18)    # 부저 18번
sensor = DistanceSensor(echo=24, trigger=23)
lcd = CharLCD(i2c_expander='PCF8574', address=0x27, port=1, cols=16, rows=2)

# 전역 변수 (거리 데이터 저장용)
current_dist = 0.0

# 2. 백그라운드 스레드: 거리 측정 및 LCD 출력
def measure_distance():
    global current_dist
    while True:
        try:
            current_dist = sensor.distance * 100
            # LCD 출력
            lcd.cursor_pos = (0, 0)
            lcd.write_string("Distance Meter")
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f"Dist: {current_dist:6.1f} cm  ")
        except:
            pass
        time.sleep(0.5)

# 거리 측정 스레드 시작
dist_thread = threading.Thread(target=measure_distance, daemon=True)
dist_thread.start()

# 3. 웹 서버 라우팅
@app.route('/')
def index():
    return render_template('led.html', distance=round(current_dist, 1))

# 제어 라우팅 부분
@app.route('/control/<device>/<action>')
def control(device, action):
    if device == 'led':
        led.on() if action == 'on' else led.off()
    elif device == 'buzzer':
        if action == 'on':
            buzzer.value = 0.5  # 소리 크기 (0.0 ~ 1.0)
            buzzer.frequency = 500 # 주파수 (숫자를 바꾸면 음높이가 변함)
        else:
            buzzer.off()
    return f"{device} {action} success"

if __name__ == '__main__':
    try:
        # --break-system-packages로 설치했으므로 바로 실행 가능
        app.run(host='0.0.0.0', port=5000)
    finally:
        lcd.clear()
        sensor.close()