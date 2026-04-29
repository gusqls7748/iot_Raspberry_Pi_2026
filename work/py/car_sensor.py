from gpiozero import DistanceSensor, PWMOutputDevice
from time import sleep

# 1. 핀 설정
# 초음파 센서: Trig=20, Echo=21
sensor = DistanceSensor(echo=21, trigger=20)
# 부저: GPIO 12번 (PWM 지원 핀)
buzzer = PWMOutputDevice(12)

# 2. 볼륨 및 음계 설정
VOLUME = 0.05  # 소리 크기 (0.01 ~ 0.1 사이 권장)
HIGH_NOTE = 523.25 # C5 (높은 도) - 위험할 때
MID_NOTE = 392.00  # G4 (솔) - 주의할 때
LOW_NOTE = 261.63  # C4 (도) - 감지 시작할 때

print("PWM 주차 보조 시스템 시작! (볼륨 조절 버전)")

try:
    while True:
        dist = sensor.distance * 100
        print(f"현재 거리: {dist:.1f} cm", end=" -> ")
        
        if dist < 5:
            print("위험!!! (연속음)")
            buzzer.frequency = HIGH_NOTE
            buzzer.value = VOLUME
            sleep(0.05) # 매우 짧게 끊어서 연속음처럼 들리게 함
            
        elif dist < 20:
            print("주의 (빠른 경고음)")
            buzzer.frequency = MID_NOTE
            buzzer.value = VOLUME
            sleep(0.2)
            buzzer.off()
            sleep(0.1)
            
        elif dist < 50:
            print("감지 중 (느린 경고음)")
            buzzer.frequency = LOW_NOTE
            buzzer.value = VOLUME
            sleep(0.5)
            buzzer.off()
            sleep(0.5)
            
        else:
            print("안전")
            buzzer.off()
            
        sleep(0.1)

except KeyboardInterrupt:
    buzzer.off()
    sensor.close()
    print("\n시스템 종료")
finally:
    buzzer.close()