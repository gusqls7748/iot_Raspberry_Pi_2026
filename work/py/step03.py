from gpiozero import DigitalOutputDevice, Button
import time

# 1. GPIO 설정
# 모터 핀 (IN1, IN2, IN3, IN4)
pins = [
    DigitalOutputDevice(17), DigitalOutputDevice(27),
    DigitalOutputDevice(22), DigitalOutputDevice(23)
]

# 상태 변수 (False: 정지, True: 회전)
is_running = False

# 스위치 핀 (GPIO 2번, GND 연결)
# pull_up=True: 버튼을 누르지 않았을 때 1(True), 눌렀을 때 0(False)
btn = Button(2, pull_up=True)

# 2. Half-step 시퀀스
SEQ = [
    [1,0,0,0], [1,1,0,0], [0,1,0,0], [0,1,1,0],
    [0,0,1,0], [0,0,1,1], [0,0,0,1], [1,0,0,1]
]

def stop_motor():
    for pin in pins:
        pin.off()

try:
    print("스위치 대기 중... (누르면 무한 회전 시작/즉시 정지)")
    
    while True:
        # 버튼이 눌렸을 때 상태를 반전 (Toggle)
        if btn.is_pressed:
            is_running = not is_running
            print("상태 변경: ", "회전 시작" if is_running else "즉시 정지")
            
            # 버튼 중복 입력 방지 및 버튼에서 손을 뗄 때까지 대기
            time.sleep(0.3) 
            while btn.is_pressed:
                time.sleep(0.01)

        if is_running:
            # 360도 제한 없이 시퀀스를 무한 반복
            for pattern in SEQ:
                # 시퀀스 도중이라도 버튼이 눌리면 즉시 중단
                if btn.is_pressed:
                    is_running = False
                    stop_motor()
                    print("회전 중 중단됨")
                    time.sleep(0.3)
                    break 
                
                # 각 핀에 신호 전송
                for pin, val in zip(pins, pattern):
                    if val: pin.on()
                    else: pin.off()
                
                # 속도 조절 (0.001 ~ 0.002 사이가 적당함)
                time.sleep(0.001)
        else:
            # 정지 상태일 때는 전원 차단
            stop_motor()
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\n사용자에 의해 종료")

finally:
    stop_motor()



# def rotate_90_degrees(delay=0.002):
#     print("버튼 감지! 90도 회전합니다.")
#     # 90도 = 512 steps. 한 cycle에 8 steps이므로 64회 반복
#     for _ in range(10):
#         for pattern in SEQ:
#             for pin, val in zip(pins, pattern):
#                 if val:
#                     pin.on()
#                 else:
#                     pin.off()
#             time.sleep(delay)
    
#     # 회전 후 모터 발열 방지를 위해 모든 핀 끄기
#     for pin in pins:
#         pin.off()

# try:
#     print("스위치를 기다리는 중... (종료하려면 Ctrl+C)")
    
#     while True:
#         # 버튼이 눌렸는지 확인 (pressed가 False일 때가 눌린 상태)
#         if btn.is_pressed:
#             rotate_90_degrees()
#             time.sleep(0.01) # 버튼 중복 입력 방지(디바운싱)
        
#         time.sleep(0.01) # CPU 부하 감소

# except KeyboardInterrupt:
#     print("\n종료합니다.")

# finally:
#     for pin in pins:
#         pin.off()