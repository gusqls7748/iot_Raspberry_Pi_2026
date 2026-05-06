from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask Server Test!!"

@app.route('/user/<username>')
def user_profile(username):
    return "user: %s" % username

@app.route('/pw/<int:pw_num>')
def user_pw(pw_num):
    return "user: %d" % pw_num

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
