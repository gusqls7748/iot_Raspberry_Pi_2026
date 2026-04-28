from gpiozero import Button, LED
from time import sleep

# 1. 두 개의 버튼과 LED 설정
button1 = Button(2)  # 첫 번째 스위치
button2 = Button(3)  # 두 번째 스위치 (GPIO 3번에 연결했다고 가정)

led_red = LED(14)    # 빨간색 LED
led_blue = LED(18)   # 파란색 LED

print("두 개의 스위치 준비 완료!")

try:
    while True:
        # 첫 번째 스위치 로직
        if button1.is_pressed:
            led_red.off()
            print("1번 버튼 눌림 -> 빨간불")
        else:
            led_red.on()

        # 두 번째 스위치 로직
        if button2.is_pressed:
            led_blue.off()
            print("2번 버튼 눌림 -> 파란불")
        else:
            led_blue.on()

        sleep(0.1)

except KeyboardInterrupt:
    print("종료")