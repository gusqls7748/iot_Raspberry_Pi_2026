import smbus
import time
from gpiozero import Button

bus = smbus.SMBus(1)
ADDR = 0x48

# GPIO 17번 버튼 설정
button = Button(17)

def read_analog(channel):
    # channel: 0~ 3
    bus.write_byte(ADDR, 0x40 | channel)
    bus.read_byte(ADDR)             # dummy read
    return bus.read_byte(ADDR)

try:
    print("조이스틱 측정을 시작합니다... (종료: Ctrl+C)")
    while True:
        x = read_analog(0)              # VRX
        y = read_analog(1)              # VRY
        sw = button.is_pressed          # 버튼 상태 (True/False)

        # 1. 상태를 저장할 변수
        direction = ""

        # 2. 방향 판단 로직 (Y값이 205이므로 범위를 210 이상으로 조정)
        if x > 180:
            direction += "▶ Right "
        elif x < 70:
            direction += "◀ LEFT "
        
        if y > 220: # 현재 Y값이 높게 나오므로 기준을 조금 높임
            direction += "▲ UP "
        elif y < 50:
            direction += "▼ DOWN "

        # 3. 중앙 판단 (X, Y 모두 범위 내일 때)
        if (110 < x < 150) and (110 < y < 150):
            direction = "● CENTER"

        # 4. 버튼 출력 처리
        btn_text = " [P]" if sw else " [ ]"

        # 5. 한 줄로 깔끔하게 출력
        print(f"X:{x:3d}, Y:{y:3d}{btn_text} | {direction}")

        time.sleep(0.2) 

except KeyboardInterrupt:
    print("\n프로그램을 종료합니다.")