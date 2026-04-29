from RPLCD.i2c import CharLCD
import time

lcd = CharLCD(
    i2c_expander='PCF8574',
    address=0x27,
    port=1,
    cols=16,
    rows=2,
    charmap='A00'
)

try:
    lcd.clear()
    lcd.write_string("GuGuDan Start")
    time.sleep(2)

    #구구단 루프 (2단 부터 9단 까지)
    for i in range(2, 10):
        lcd.clear()
        # 첫 번째 줄에 현재 단 표시
        lcd.cursor_pos = (0, 0)
        lcd.write_string(f"*** Step {i} ***")
        time.sleep(1)

        for j in range(1, 10):
            # 두 번째 줄만 지우고 결과 출력( 커서 위치 활용)
            lcd.cursor_pos = (1, 0)
            #공백을 줘서 이전 글자를 지워줌
            lcd.write_string(f"{i} x {j} = {i*j}    ")

        # 출력 속도 조절 (0.8초마다 다음 식 출력)
        time.sleep(0.8)

    lcd.clear()
    lcd.write_string("All Finished!")
    time.sleep(2)

except KeyboardInterrupt:
    print("사용자에 의해 중단됨")

finally:
    lcd.clear()
    lcd.close(clear=True)
    
# lcd.cursor_pos = (1,0): 커서 위치 지정
# lcd.display_enabled = False / True: 디스플레이 오프
# lcd.backlight_enabled = True / False: 백라이트