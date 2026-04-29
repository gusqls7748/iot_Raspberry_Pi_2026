from gpiozero import DistanceSensor 
from signal import pause

sensor = DistanceSensor(
    echo=21, 
    trigger=20,
    threshold_distance=0.3)

sensor.when_in_range = lambda: print("30cm 이내 접근")
sensor.when_out_of_range = lambda: print("떨어짐")


try:
    pause()
except KeyboardInterrupt:
    sensor.close()