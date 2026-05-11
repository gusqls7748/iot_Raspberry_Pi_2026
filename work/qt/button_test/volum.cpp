#include "volum.h"
#include <wiringPi.h>
#include <softPwm.h>

Volum::Volum(int pin) : buzzerPin(pin) {
    pinMode(buzzerPin, OUTPUT);
    softPwmCreate(buzzerPin, 0, 100);
}

void Volum::turnOff() {
    softPwmWrite(buzzerPin, 0);
}

void Volum::setVolume(int volume) {
    if (volume < 0) volume = 0;
    if (volume > 100) volume = 100;
    softPwmWrite(buzzerPin, volume);
}
