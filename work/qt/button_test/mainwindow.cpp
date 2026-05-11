#include "mainwindow.h"
#include "./ui_mainwindow.h"
#include <fcntl.h>
#include <unistd.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include <wiringPi.h>

// LCD 설정
#define I2C_ADDR 0x27
#define LINE1 0x80
#define LINE2 0xC0
#define LCD_CMD 0
#define LCD_CHR 1
#define ENABLE 0b00000100
#define LCD_BACKLIGHT 0x08

void lcd_send_byte(int fd, int bits, int mode) {
    int high = mode | (bits & 0xF0) | LCD_BACKLIGHT;
    int low = mode | ((bits << 4) & 0xF0) | LCD_BACKLIGHT;
    auto toggle = [&](int b) {
        write(fd, &b, 1);
        int eb = b | ENABLE; write(fd, &eb, 1); usleep(500);
        int db = b & ~ENABLE; write(fd, &db, 1); usleep(500);
    };
    toggle(high); toggle(low);
}

void lcd_init(int fd) {
    for(int b : {0x33, 0x32, 0x06, 0x0C, 0x28, 0x01}) lcd_send_byte(fd, b, LCD_CMD);
}

void lcd_string(int fd, const char *s, int line) {
    if(fd < 0) return;
    lcd_send_byte(fd, line, LCD_CMD);
    while(*s) lcd_send_byte(fd, *(s++), LCD_CHR);
}

MainWindow::MainWindow(QWidget *parent)
    : QMainWindow(parent), ui(new Ui::MainWindow) {
    ui->setupUi(this);

    if (wiringPiSetupGpio() == -1) return;

    pinMode(23, OUTPUT); // Trig
    pinMode(24, INPUT);  // Echo
    pinMode(17, OUTPUT); // LED
    buzzerControl = new Volum(18);

    lcd_fd = open("/dev/i2c-1", O_RDWR);
    if (lcd_fd >= 0) {
        ioctl(lcd_fd, I2C_SLAVE, I2C_ADDR);
        lcd_init(lcd_fd);
        lcd_string(lcd_fd, "System Ready", LINE1);
        lcd_string(lcd_fd, "Status: OFF", LINE2);
    }

    timer = new QTimer(this);
    connect(timer, &QTimer::timeout, this, &MainWindow::updateDistance);
    timer->start(100);
}

MainWindow::~MainWindow() {
    if (lcd_fd >= 0) ::close(lcd_fd);
    delete ui;
}

void MainWindow::on_pushButton_clicked() { // ON 버튼
    isSystemOn = true;
    last_buzzer_state = false;

    digitalWrite(17, HIGH); // 실제 LED 켜기

    // [색깔 통일] 켤 때 빨간색
    ui->label_LED->setStyleSheet("background-color: red; border-radius: 20px;");
    ui->label_distance->setStyleSheet("background-color: red; border-radius: 20px; color: white;");
    ui->label_distance->setText("Monitoring...");

    if (lcd_fd >= 0) {
        lcd_string(lcd_fd, "System: ON      ", LINE1);
        lcd_string(lcd_fd, "Monitoring...   ", LINE2);
    }
}

void MainWindow::on_pushButton_2_clicked() { // OFF 버튼
    isSystemOn = false;

    digitalWrite(17, LOW); // 실제 LED 끄기
    if (buzzerControl) buzzerControl->turnOff();

    // [색깔 통일] 끌 때 파란색
    ui->label_LED->setStyleSheet("background-color: blue; border-radius: 20px;");
    ui->label_distance->setStyleSheet("background-color: blue; border-radius: 20px; color: white;");
    ui->label_distance->setText("OFF");

    if (lcd_fd >= 0) {
        lcd_string(lcd_fd, "System: OFF     ", LINE1);
        lcd_string(lcd_fd, "Press ON Button ", LINE2);
    }
}

void MainWindow::updateDistance() {
    if (!isSystemOn) return;

    // 초음파 측정 로칭 (기존과 동일)
    digitalWrite(23, LOW); delayMicroseconds(2);
    digitalWrite(23, HIGH); delayMicroseconds(10);
    digitalWrite(23, LOW);

    long s = micros();
    while (digitalRead(24) == LOW) if (micros() - s > 30000) return;
    long start = micros();
    while (digitalRead(24) == HIGH) if (micros() - start > 30000) break;
    double dist = (micros() - start) * 0.0343 / 2.0;

    if (dist > 2.0 && dist < 400.0) {
        // 1. 화면(Qt GUI) 업데이트
        ui->label_distance->setText(QString::number(dist, 'f', 1) + " cm");

        // 2. LCD 실시간 거리 표시 (2번째 라인에 계속 업데이트)
        // %-16f 처럼 공백을 채워줘야 예전 글자가 안 남습니다.
        char lcd_msg[17];
        sprintf(lcd_msg, "Dist: %.1f cm   ", dist);
        lcd_string(lcd_fd, lcd_msg, LINE2);

        bool danger = (dist < 10.0);
        if (danger != last_buzzer_state) {
            if (danger) {
                buzzerControl->setVolume(ui->verticalSlider->value());
                ui->label_LED->setStyleSheet("background-color: red; border-radius: 20px;");
                ui->label_distance->setStyleSheet("background-color: red; border-radius: 20px; color: white;");

                // 위험할 때 1번째 라인 변경
                lcd_string(lcd_fd, "!!! DANGER !!!  ", LINE1);
            } else {
                buzzerControl->turnOff();
                ui->label_LED->setStyleSheet("background-color: blue; border-radius: 20px;");
                ui->label_distance->setStyleSheet("background-color: blue; border-radius: 20px; color: white;");

                // 안전할 때 1번째 라인 복구
                lcd_string(lcd_fd, "System: ON      ", LINE1);
            }
            last_buzzer_state = danger;
        }
    }
}

void MainWindow::on_verticalSlider_valueChanged(int value) {
    if (isSystemOn && last_buzzer_state) buzzerControl->setVolume(value);
}
