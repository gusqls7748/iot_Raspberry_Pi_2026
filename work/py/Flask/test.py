# from gpiozero import LED
# from time import sleep

# led = LED(17)

# while True:
#     led.on()
#     sleep(0.5)
#     led.off()

# from gpiozero import Buzzer
# from time import sleep

# #GPIO 18번 핀에 부저의 +극을 연결한 경우
# buzzer = Buzzer(18)

# while True:
#     buzzer.on() #부저켜기
#     print("Buzzer on")
#     sleep(1)

#     buzzer.off() #부저끄기
#     print("Buzzer off")
#     sleep(1)

# from gpiozero import DistanceSensor
# from time import sleep

# # trigger=23, echo=24 핀 설정
# # max_distance는 보통 2(미터) 정도로 잡습니다.
# sensor = DistanceSensor(echo=24, trigger=23)

# print("거리 측정 시작! (종료하려면 Ctrl+C)")

# try:
#     while True:
#         # sensor.distance는 '미터' 단위이므로 100을 곱해 'cm'로 만듭니다.
#         distance_cm = sensor.distance * 100
#         print(f"거리: {distance_cm:.2f} cm")
#         sleep(1)
        
# except KeyboardInterrupt:
#     print("측정 종료")

from gpiozero import DistanceSensor
from RPLCD.i2c import CharLCD
import time

# 1. 초음파 센서 설정 (기존 핀 유지)
sensor = DistanceSensor(echo=24, trigger=23)

# 2. LCD 설정 (기존 설정 유지)
lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=1,
    cols=16,
    rows=2,
    charmap='A00'
)

print("거리 측정 및 LCD 표시 시스템 시작!")

try:
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Distance Meter")
    
    while True:
        # 거리 측정 (cm 단위)
        dist = sensor.distance * 100
        
        # LCD 두 번째 줄에 거리값 출력
        lcd.cursor_pos = (1, 0)
        # 이전 글자가 남지 않도록 공백을 넉넉히 줌
        lcd.write_string(f"Dist: {dist:6.1f} cm  ")
        
        # 터미널에도 동시에 출력 (확인용)
        print(f"현재 측정 거리: {dist:.1f} cm")
        
        # 0.5초마다 갱신
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n시스템 종료")

finally:
    lcd.clear()
    lcd.close(clear=True)
    sensor.close()