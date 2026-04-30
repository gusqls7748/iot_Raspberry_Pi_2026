from gpiozero import DigitalOutputDevice, Button
from time import sleep

KEYS = [
    ['1','2','3','A'],
    ['4','5','6','B'],
    ['7','8','9','C'],
    ['*','0','#','D']
]

# KEYS = [
#     ['1','4','7','0'],
#     ['2','5','8','#'],
#     ['3','6','9','*'],
#     ['A','B','C','D']
# ]

COL_PINS = [21, 20, 16, 12]
ROW_PINS = [5, 6, 13, 19]

rows = [DigitalOutputDevice(pin, active_high=True, initial_value=False)
        for pin in ROW_PINS]

cols = [Button(pin, pull_up=False)
        for pin in COL_PINS]

def scan_keypad():
    for row_index, row in enumerate(rows):
        for r in rows:
            r.off()
        row.on()
        sleep(0.001)
        for col_index, col in enumerate(cols):
            if col.is_pressed:
                return KEYS[row_index][col_index]
    return None

try:
    last_key = None
    while True:
        key =scan_keypad()

        if key is not None and key != last_key:
            print("Pressed:", key)
            last_key = key

        if key is None:
            last_key = None

        sleep(0.05)

except KeyboardInterrupt:
    print("Exit")

finally:
    for r in rows:
        r.off()

