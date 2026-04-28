 from gpiozero import LED
 from time import sleep

 led = LED(14)
 led2 = LED(15)
 led3 = LED(18)

 while True:
    led.on()
    sleep(0.5)
    led.off()

    # 2번만 켜기
    led2.on()
    sleep(0.5)
    led2.off()

    #3번만 켜기
    led3.on()
    sleep(0.5)
    led3.off()
    
    
    
    

