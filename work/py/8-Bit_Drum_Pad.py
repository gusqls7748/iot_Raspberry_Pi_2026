from gpiozero import DigitalOutputDevice, Button, TonalBuzzer
from gpiozero.tones import Tone
from RPLCD.i2c import CharLCD
from time import sleep

# 1. 하드웨어 설정
lcd = CharLCD('PCF8574', 0x27, port=1, charmap='A00')
buzzer = TonalBuzzer(4) # 부저 GPIO 4

# 2. 키패드 설정
KEYS = [['1','2','3','A'], ['4','5','6','B'], ['7','8','9','C'], ['*','0','#','D']]
COL_PINS = [21, 20, 16, 12]
ROW_PINS = [5, 6, 13, 19]
rows = [DigitalOutputDevice(pin, active_high=True, initial_value=False) for pin in ROW_PINS]
cols = [Button(pin, pull_up=False) for pin in COL_PINS]

# 3. 데이터 설정 (안전한 저음역대 중심)
MARIO_MELODY = ["E4", "E4", "0", "E4", "0", "C4", "E4", "0", "G4", "0", "G3", "0"]
BEATS = [0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.12, 0.24, 0.24, 0.24, 0.24]

SOUND_MAP = {
    '1': 'E4', '2': 'C4', '3': 'G4', 'A': 'G3',
    '4': 'F4', '5': 'D4', '6': 'B3', 'B': 'A3',
    '7': 'E3', '8': 'C3', '9': 'G2', 'C': 'F3',
    '*': 'A2', '0': 'B2', '#': 'C2', 'D': 'D2'
}

def play_auto_mario():
    lcd.clear()
    lcd.write_string("Auto Playing...")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Super Mario!")
    
    for note, beat in zip(MARIO_MELODY, BEATS):
        if note != "0":
            try:
                buzzer.play(Tone(note))
            except: pass
        sleep(beat)
        buzzer.stop()
        sleep(0.02)

def scan_keypad():
    for row_index, row in enumerate(rows):
        for r in rows: r.off()
        row.on()
        for col_index, col in enumerate(cols):
            if col.is_pressed:
                return KEYS[row_index][col_index]
    return None

try:
    # [단계 1] 자동 연주
    play_auto_mario()
    
    # [단계 2] DJ 모드 전환 안내
    lcd.clear()
    lcd.write_string("DJ Mode Start!")
    lcd.cursor_pos = (1, 0)
    lcd.write_string("Press Any Key")
    sleep(1.5)
    
    last_key = None
    while True:
        key = scan_keypad()
        if key is not None:
            if key in SOUND_MAP:
                note = SOUND_MAP[key]
                try:
                    buzzer.play(Tone(note))
                    lcd.clear()
                    lcd.write_string(f"Key: {key}")
                    lcd.cursor_pos = (1, 0)
                    lcd.write_string(f"Note: {note}")
                except: pass
            last_key = key
        else:
            buzzer.stop()
            if last_key is not None:
                last_key = None
        sleep(0.01)

except KeyboardInterrupt:
    print("\nExit")
finally:
    buzzer.stop()
    for r in rows: r.off()
    lcd.clear()
    lcd.write_string("Program Stopped")