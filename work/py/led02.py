from gpiozero import Button, LED
from time import sleep

# 1. 하드웨어 설정
button1 = Button(4)
button2 = Button(17)
led_red = LED(14)
led_blue = LED(18)

# 2. 초기 상태 설정 (시작 시 보라색)
color_state = 0
led_red.on()
led_blue.on()

# 3. [이벤트 방식] 2번 버튼 설정
# 함수를 정의해서 print문까지 나오게 하면 더 좋습니다.
def button2_pressed():
    led_blue.off()
    print(">>> 2번 버튼 누름: 파란색 강제 종료")

def button2_released():
    # 2번 버튼을 떼면 현재 모드(color_state)에 상관없이 일단 다시 켭니다.
    led_blue.on()
    print(">>> 2번 버튼 뗌: 파란색 복구")

# 이벤트 예약 (while문 밖에서 한 번만 설정하면 끝!)
button2.when_pressed = button2_pressed
button2.when_released = button2_released

print("통합 프로그램 시작!")
print("1번 버튼: 누를 때마다 모드 변경 (보라->파랑->빨강->꺼짐)")
print("2번 버튼: 누르는 동안 파란색만 끄기 (이벤트 방식)")

try:
    while True: # 반복문 시작
        # [반복문 방식] 1번 버튼의 상태 제어
        if button1.is_pressed:
            color_state = (color_state + 1) % 4
            print(f"[모드 변경] 현재 상태: {color_state}")

            if color_state == 0:
                led_red.on()
                led_blue.on()
                print("결과: 모두 꺼짐")
            elif color_state == 1:
                led_red.off()
                led_blue.on()
                print("결과: 빨간색")
            elif color_state == 2:
                led_red.on()
                led_blue.off()
                print("결과: 파란색")
            else:
                led_red.off()
                led_blue.off()
                print("결과: 모두 켜짐")

            # 손 뗄 때까지 대기 (한 번의 클릭에 한 번만 변경되도록)
            while button1.is_pressed:
                sleep(0.01)
        
        sleep(0.1) # CPU 휴식

except KeyboardInterrupt:
    print("\n중료 중...")

finally:
    # 프로그램 종료 시 모든 LED 안전하게 끄기
    led_red.off()
    led_blue.off()
    led_red.close()
    led_blue.close()
    print("안전하게 종료되었습니다.")