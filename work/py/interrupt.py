#이벤트 기반#
from gpiozero import LED, Button
from signal import pause

led_red = LED(14)
led_blue = LED(18)
button1 = Button(2)
button2 = Button(3)

# 2. 초기 상태 설정
color_state = 0
led_red.on()   # 시작 시 보라색
led_blue.on()

def button_pressed():
    led.on()
    print("BUTTON PRESSED")

def button_released():
    led.off()
    print("BUTTON RELEASED")

button.when_pressed = button_pressed
button.when_released = button_released

try:
    pause()
finally:
    led_red.off()
    led_red.close()
    led_blue.off()
    led_blue.close()
    print("\n exit")