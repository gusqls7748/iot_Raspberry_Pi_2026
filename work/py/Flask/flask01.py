from flask import Flask

app = Flask(__name__)  # _name_ 을 __name__ 으로 수정

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":  # _name_ 을 __name__ 으로 수정
    app.run(host='0.0.0.0', port=8989, debug=True) # 포트 번호(8989)를 명시하면 더 확실합니다.