from gpiozero import DigitalOutputDevice, Button, TonalBuzzer
from gpiozero.tones import Tone
from RPLCD.i2c import CharLCD
from time import sleep

# 1. LCD 및 부저 설정
lcd = CharLCD('PCF8574', 0x27, port=1, charmap='A00')
buzzer = TonalBuzzer(4) # GPIO 4번에 연결

# 2. 키패드 설정 (기존 유지)
KEYS = [['1','2','3','A'], ['4','5','6','B'], ['7','8','9','C'], ['*','0','#','D']]
COL_PINS = [21, 20, 16, 12]
ROW_PINS = [5, 6, 13, 19]
rows = [DigitalOutputDevice(pin, active_high=True, initial_value=False) for pin in ROW_PINS]
cols = [Button(pin, pull_up=False) for pin in COL_PINS]

PASSWORD = ""
input_buffer = ""
is_setup_done = False

def play_sound(result):
    if result == "success":
        # 도(C4), 레(D4), 미(E4) - 부드러운 상승음
        for note in ["C4", "D4", "E4"]:
            buzzer.play(Tone(note))
            sleep(0.2)
        buzzer.stop()
    elif result == "fail":
        # 솔(G4), 솔(G4), 솔(G4) - 같은 낮은 음을 짧고 강하게 반복
        # 5옥타브(G5) 대신 안전한 4옥타브(G4)를 사용합니다.
        for _ in range(3):
            buzzer.play(Tone("G4"))
            sleep(0.1)
            buzzer.stop()
            sleep(0.1)

def scan_keypad():
    for row_index, row in enumerate(rows):
        for r in rows: r.off()
        row.on()
        sleep(0.01)
        for col_index, col in enumerate(cols):
            if col.is_pressed:
                return KEYS[row_index][col_index]
    return None

def update_lcd(line1, line2=""):
    lcd.clear()
    lcd.cursor_pos = (0, 0)
    lcd.write_string(line1)
    lcd.cursor_pos = (1, 0)
    lcd.write_string(line2)

try:
    update_lcd("Set Initial PW:", "Input 4 digits")
    last_key = None

    while True:
        key = scan_keypad()
        if key is not None and key != last_key:
            if not is_setup_done:
                if key.isdigit() and len(input_buffer) < 4:
                    input_buffer += key
                    update_lcd("Set Initial PW:", input_buffer)
                elif key == '#' and len(input_buffer) == 4:
                    PASSWORD = input_buffer
                    is_setup_done = True
                    input_buffer = ""
                    update_lcd("PW Set Done!", f"PW is {PASSWORD}")
                    play_sound("success") # 설정 완료 시 성공 음
                    sleep(1)
                    update_lcd("Enter Password:", "")
            else:
                if key == '#':
                    if input_buffer == PASSWORD:
                        update_lcd("Access Granted!", "Welcome!")
                        play_sound("success") # 성공 음 출력
                        sleep(1)
                    else:
                        update_lcd("Access Denied!", "Wrong PW")
                        play_sound("fail") # 실패 음 출력
                        sleep(1)
                    input_buffer = ""
                    update_lcd("Enter Password:", "")
                elif key == '*':
                    input_buffer = ""
                    update_lcd("Enter Password:", "")
                elif key.isdigit() and len(input_buffer) < 4:
                    input_buffer += key
                    update_lcd("Enter Password:", "*" * len(input_buffer))

            last_key = key
            sleep(0.2)
        if key is None:
            last_key = None
        sleep(0.05)

except KeyboardInterrupt:
    print("Exit")
    lcd.clear()
finally:
    for r in rows: r.off()
    buzzer.stop()