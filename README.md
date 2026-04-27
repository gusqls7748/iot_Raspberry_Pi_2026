<<<<<<< HEAD
# iot_Raspberry_Pi_2026
2026년 Iot개발 라즈베리파이 리포지토리

- 라즈베리파이 다운

- https://www.raspberrypi.com/software/

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

rpi

raspi

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

- https://www.realvnc.com/en/connect/download/viewer/

![alt text](image-6.png)

그다음 cmd 에서

ssh rpi@192.168.0.2
비번 입력후

```
sudo apt update
sudo apt apgrade를 한다.
```

![alt text](image-8.png)

![alt text](image-9.png)

아이디 비번 입력한다.

![alt text](image-10.png)

![alt text](image-12.png)

- 한글 설치
![alt text](image-13.png)

```
    1  sudo apt update
    2  sudo aup upgrade
    3  sudo apt upgrade
    4  sudo apt update
    5  sudo apt upgrade
    6  sudo raspi-config
    7  sudo apt install fonts-nanum fonts-nanum-extra
    8  sudo apt install fonts-unfonts-core
    9  sudo apt install ibus
   10  sudo apt install ibus-hangul
   11  ibus-setup
   12  ibus restart
   13  history
   14 sudo apt install libgpiod-dev gpiod -y
   15 uname -1
   16 uname -a
   17 ip a

    autoindent
    linenumbers
    tabsize3
```

![alt text](image-14.png)

- ls -l
![alt text](image-15.png)

- cat /etc/os-release
![alt text](image-16.png)

- uname
![alt text](image-17.png)

- free -h
![alt text](image-18.png)

## python 다운로드
```
81  ls
   82  cd work
   83  mkdir py
   84  ls
   85  cd py
   86  sudo apt install python3-libgpiod
   87  cd

```

## 가상환경

```
1. 가상환경 전용 폴더 만들고 들어가기
    mkdir -p ~/venvs
    cd ~/venvs
2. 가상환경 실제로 생성하기
    python3 -m venv venv
3. 가상환경 활성화(켜기)
    source venv/bin/activate
   source ./.venv/bin/activate

```

pinout

=======
# iot_Raspberry_Pi_2026
2026년 Iot개발 라즈베리파이 리포지토리

- 라즈베리파이 다운

- https://www.raspberrypi.com/software/

![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

rpi

raspi

![alt text](image-3.png)

![alt text](image-4.png)

![alt text](image-5.png)

- https://www.realvnc.com/en/connect/download/viewer/

![alt text](image-6.png)

그다음 cmd 에서

ssh rpi@192.168.0.2
비번 입력후

```
sudo apt update
sudo apt apgrade를 한다.
```

![alt text](image-8.png)

![alt text](image-9.png)

아이디 비번 입력한다.

![alt text](image-10.png)

![alt text](image-12.png)

- 한글 설치
![alt text](image-13.png)

```
    1  sudo apt update
    2  sudo aup upgrade
    3  sudo apt upgrade
    4  sudo apt update
    5  sudo apt upgrade
    6  sudo raspi-config
    7  sudo apt install fonts-nanum fonts-nanum-extra
    8  sudo apt install fonts-unfonts-core
    9  sudo apt install ibus
   10  sudo apt install ibus-hangul
   11  ibus-setup
   12  ibus restart
   13  history
   14 sudo apt install libgpiod-dev gpiod -y
   15 uname -1
   16 uname -a
   17 ip a

    autoindent
    linenumbers
    tabsize3
```

![alt text](image-14.png)

- ls -l
![alt text](image-15.png)

- cat /etc/os-release
![alt text](image-16.png)

- uname
![alt text](image-17.png)

- free -h
![alt text](image-18.png)

## python 다운로드
```
81  ls
   82  cd work
   83  mkdir py
   84  ls
   85  cd py
   86  sudo apt install python3-libgpiod
   87  cd

```

## 가상환경

```
1. 가상환경 전용 폴더 만들고 들어가기
    mkdir -p ~/venvs
    cd ~/venvs
2. 가상환경 실제로 생성하기
    python3 -m venv venv
3. 가상환경 활성화(켜기)
    source venv/bin/activate
   source ./.venv/bin/activate

```

pinout

>>>>>>> c3c825e6ce6f0283e5fc647ca961d7dfe457009c
![alt text](image-19.png)