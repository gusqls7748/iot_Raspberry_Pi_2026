#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QTimer>
#include "volum.h"

QT_BEGIN_NAMESPACE
namespace Ui { class MainWindow; }
QT_END_NAMESPACE

class MainWindow : public QMainWindow {
    Q_OBJECT

public:
    MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void updateDistance();
    void on_pushButton_clicked();      // ON 버튼
    void on_pushButton_2_clicked();    // OFF 버튼
    void on_verticalSlider_valueChanged(int value);

private:
    Ui::MainWindow *ui;
    QTimer *timer;
    int lcd_fd = -1;
    bool isSystemOn = false;
    bool last_buzzer_state = false;
    Volum *buzzerControl;
};
#endif
