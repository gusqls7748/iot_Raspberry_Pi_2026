from flask import Flask, render_template, redirect, url_for
from gpiozero import LED

app = Flask(__name__)

# 하드웨어 연결에 맞춰 17번 핀 사용
led = LED(17)

@app.route("/")
def index():
    # 현재 LED 상태를 읽어와서 템플릿으로 전달
    state = "ON" if led.is_lit else "OFF"
    return render_template("led.html", state=state)

@app.route("/led/on", methods=["GET", "POST"]) # methods (s 추가)
def led_on():
    led.on()
    return redirect(url_for("index")) # 함수명 index로 변경

@app.route("/led/off", methods=["GET", "POST"]) # methods (s 추가)
def led_off():
    led.off()
    return redirect(url_for("index")) # 함수명 index로 변경

if __name__ == "__main__": # __main__ 으로 변경
    try:
        # port=5000 으로 변경
        app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
    finally:
        led.off()
        led.close() # .close() 로 변경