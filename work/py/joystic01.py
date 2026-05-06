# import smbus
# import time 
# from gpiozero import Button

# bus = smbus.SMBus(1)
# ADDR = 0x48                     #PCF8591 기본주소

# button = Button(17)

# def read_abc(channel):
#     bus.write_byte(ADDR, 0x40 | channel)
#     bus.read_byte(ADDR)
#     return bus.read_byte(ADDR)

# try:
#     while True:
#         x = read_abc(0)
#         y = read_abc(1)
#         sw = button.is_pressed

#         print(f"x: {x}, Y: {y}, SW: {sw}")
#         time.sleep(0.5)

# except KeyboardInterrupt:
#     print("종료")

import smbus
import time 


bus = smbus.SMBus(1)
                #PCF8591 기본주소

ADDR = 0x48

def read_abc(channel):
    bus.write_byte(ADDR, 0x40 | channel)
    bus.read_byte(ADDR)
    return bus.read_byte(ADDR)

try:
    while True:
        x = read_abc(0)
        y = read_abc(1)
        sw = read_abc(2)

        print(f"x: {x}, Y: {y}, SW: {sw}")
        time.sleep(0.5)

except KeyboardInterrupt:
    print("종료")