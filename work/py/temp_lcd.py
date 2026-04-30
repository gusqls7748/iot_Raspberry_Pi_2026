import time
import board
import adafruit_dht
from RPLCD.i2c import CharLCD

# 1. DHT11 설정 (GPIO 4)
dht_device = adafruit_dht.DHT11(board.D4)

# 2. LCD 설정 (I2C 주소는 보통 0x27 또는 0x3f 입니다)
# 연결하신 GPIO 21(SDA), 20(SCL)은 라즈베리파이의 기본 I2C 버스 1번을 사용합니다.
lcd = CharLCD('PCF8574', 0x27, port=1, charmap='A00')

def display_data():
    try:
        print("측정 및 LCD 출력 시작...")
        while True:
            try:
                # 온습도 데이터 읽기
                temperature = dht_device.temperature
                humidity = dht_device.humidity

                if temperature is not None and humidity is not None:
                    # 콘솔 출력
                    print(f"Temp: {temperature:.1f}C, Hum: {humidity:.1f}%")
                    
                    # LCD 출력
                    lcd.clear()
                    lcd.cursor_pos = (0, 0)
                    lcd.write_string(f"Temp: {temperature:.1f}C")
                    lcd.cursor_pos = (1, 0)
                    lcd.write_string(f"Hum:  {humidity:.1f}%")
                
                else:
                    lcd.clear()
                    lcd.write_string("Sensor Error")

            except RuntimeError as error:
                # DHT 센서 특성상 발생하는 일시적 오류 무시
                print(f"Reading error: {error.args[0]}")
            
            time.sleep(2.0)

    except KeyboardInterrupt:
        print("프로그램 종료")
        lcd.clear()
        lcd.write_string("Program Stopped")
    
    finally:
        dht_device.exit()

if __name__ == "__main__":
    display_data()