# -*- coding:UTF-8 -*-

from flask import request
from flask import Flask

#新建一个Flask可运行实体
app = Flask(__name__)

#在app上绑定URL路由信息
@app.route("/", methods=["GET", "POST"])
def home():
    return "hello, flask"

@app.route("/signin", methods=["GET"])
def signin_form():
    return  '''<form action="/signin" method="POST">
                <p><input name="usr"></p>
                <p><input name="pwd" type="password"></p>
                <p><button type="submit">Sign In</button></p>
              </form>'''

@app.route("/signin", methods=["POST"])
def signin():
    if request.form["usr"] == "admin" and request.form["pwd"] == "xx":
        return "<h3>hello, %s</h3>" %request.form["usr"]
    else:
        return "<h3>user name or password error.</h3>"

if (__name__ == "__main__"):
    app.run()