#ifndef VOLUM_H
#define VOLUM_H

class Volum {
public:
    Volum(int pin);
    void turnOff();
    void setVolume(int volume);

private:
    int buzzerPin;
};

#endif
