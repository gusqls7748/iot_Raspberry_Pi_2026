# pip install adafruit-circuitpython-dht
import time
import board
import adafruit_dht

# DATA 핀: GPIO4 = board.D4 = 물리핀 7번
dht = adafruit_dht.DHT11(board.D4)

try:
    print("DHT11 온습도 측정 시작...")

    while True:
        try:
            temp = dht.temperature
            hum = dht.humidity

            # 오타 수정: humi -> hum (위에서 정의한 변수명과 일치시켜야 함)
            if temp is not None and hum is not None:
                print(f"Temp: {temp:.1f}'C / Humi: {hum:.1f}%")
            else:
                # 오타 수정: Faild -> Failed
                print("Failed to measure")
            
        except RuntimeError as e:
            # DHT11은 읽기 타이밍 민감도가 높아 에러가 잦으므로 그대로 둡니다.
            print("Reading failed, retrying:", e)

        time.sleep(2)

except KeyboardInterrupt:
    print("exit")

finally:
    dht.exit()