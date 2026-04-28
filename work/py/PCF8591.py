# import smbus
# import time

# bus = smbus.SMBus(1)
# ADDR = 0x48

# def read_cds():
#     # 0x41은 보통 PCF8591 보드에 달린 조도센서(AIN1) 채널입니다.
#     bus.write_byte(ADDR, 0x40) 
#     bus.read_byte(ADDR)        # 가짜 읽기(Dummy)
#     return bus.read_byte(ADDR)

# print("조도 센서 모니터링 시작 (Ctrl+C로 종료)")

# try:
#     while True:
#         val = read_cds()
        
#         # 값이 어떻게 변하는지 별표(*) 개수로 시각화해보기
#         # 숫자가 작을수록(밝을수록) 별이 많아지게 표현
#         visual = "*" * (val // 5)
#         print(f"값: {val:3} | {visual}")
        
#         time.sleep(0.2) # 조금 더 빠르게 확인

# except KeyboardInterrupt:
#     print("\n중단됨")

import smbus
import time

bus = smbus.SMBus(1)
ADDR = 0x48
def read_cds():
    bus.write_byte(ADDR, 0x40) # AIN1
    bus.read_byte(ADDR)        # dummy
    return bus.read_byte(ADDR)
try:
    while True:
        val = read_cds()
        print("CDS:", val)
        time.sleep(0.5)
except KeyboardInterrupt:
    print("종 료")