import smbus
import time
from gpiozero import LED

# 1. 설정
address = 0x48           # PCF8591 주소
bus = smbus.SMBus(1)     # I2C 버스 번호
led = LED(18)            # GPIO 18번에 연결한 LED

def read_cds():
    # AIN0 채널에서 조도 센서 값 읽기 (0~255)
    bus.write_byte(address, 0x42) 
    bus.read_byte(address)         # 가짜 읽기 (더미)
    return bus.read_byte(address)  # 실제 값 읽기

try:
    print("자동 조명 시스템 시작 (Ctrl+C로 종료)")
    while True:
        cds_value = read_cds()
        print(f"현재 밝기: {cds_value}")

        # 어두워지면(값이 낮아지면) LED 켜기 
        # (기준값 100은 환경에 따라 수정하세요)
        if cds_value < 100:
            led.on()
            print("상태: 어두움 - LED ON")
        else:
            led.off()
            print("상태: 밝음 - LED OFF")

        time.sleep(0.5)

except KeyboardInterrupt:
    print("\n시스템 종료")
    led.off()