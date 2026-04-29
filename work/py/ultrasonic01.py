from gpiozero import DistanceSensor 
from time import sleep

sensor = DistanceSensor(echo=21, trigger=20)

try:
    while True:
        print('Distance: ' , sensor.distance, 'm')
        sleep(1)
except KeyboardInterrupt:
    sensor.close()