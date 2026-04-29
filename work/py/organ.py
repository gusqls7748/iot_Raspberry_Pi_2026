# import sys
# import tty
# import termios
# from gpiozero import PWMOutputDevice

# # 1. 부저 설정
# buzzer = PWMOutputDevice(21)
# VOLUME = 0.01

# # 2. 키보드 매핑
# key_notes = {
#     'a': 261.63, 's': 293.66, 'd': 329.63, 'f': 349.23,
#     'g': 392.00, 'h': 440.00, 'j': 493.88, 'k': 523.25
# }

# def get_key():
#     """터미널에서 키 입력을 실시간으로 읽는 함수"""
#     fd = sys.stdin.fileno()
#     old_settings = termios.tcgetattr(fd)
#     try:
#         tty.setraw(sys.stdin.fileno())
#         ch = sys.stdin.read(1)
#     finally:
#         termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
#     return ch

# print("전자 오르간 시작! (a,s,d,f,g,h,j,k 연주 / 'q' 종료)")

# try:
#     while True:
#         key = get_key()
        
#         if key == 'q':  # q 누르면 종료
#             break
        
#         if key in key_notes:
#             buzzer.frequency = key_notes[key]
#             buzzer.value = VOLUME
#             import time
#             time.sleep(0.2)  # 터미널 방식 특성상 살짝 끊어서 연주
#             buzzer.value = 0

# except KeyboardInterrupt:
#     pass
# finally:
#     buzzer.close()
#     print("\n종료되었습니다.")

from gpiozero import PWMOutputDevice
from time import sleep

# 1. 부저 설정 (GPIO 21번)
buzzer = PWMOutputDevice(21)
VOLUME = 0.01  # 수업용 아주 작은 소리

# 2. 키보드 매핑
key_notes = {
    'a': 261.63, 's': 293.66, 'd': 329.63, 'f': 349.23,
    'g': 392.00, 'h': 440.00, 'j': 493.88, 'k': 523.25
}

print("--- 전자 오르간 (input 버전) ---")
print("사용법: a, s, d... 입력 후 Enter를 치세요.")
print("종료하려면 'q'를 입력하세요.")

try:
    while True:
        # 사용자로부터 입력을 받음
        user_input = input("음표 입력 (a,s,d,f,g,h,j,k): ").lower()

        if user_input == 'q':
            break
        
        # 입력된 글자가 매핑 테이블에 있는지 확인
        if user_input in key_notes:
            buzzer.frequency = key_notes[user_input]
            buzzer.value = VOLUME
            sleep(0.5)     # 0.5초 동안 소리 내기
            buzzer.value = 0
        else:
            print("알 수 없는 키입니다.")

finally:
    buzzer.close()
    print("프로그램 종료")