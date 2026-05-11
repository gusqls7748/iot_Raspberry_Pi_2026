from gpiozero import Buzzer
from time import sleep

#GPIO 21번 핀에 부저의 +극을 연결한 경우
buzzer = Buzzer(18)

while True:
    buzzer.on() #부저켜기
    print("Buzzer on")
    sleep(1)

    buzzer.off() #부저끄기
    print("Buzzer off")
    sleep(1)
