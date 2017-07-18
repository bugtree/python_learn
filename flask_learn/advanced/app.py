# -*- coding:UTF-8 -*-

from flask import request
from flask import Flask
from flask import render_template 

#新建一个Flask可运行实体
app = Flask(__name__)

#在app上绑定URL路由信
@app.route("/", methods=["GET", "POST"])
def home():
    return render_template("home.html") 

@app.route("/signin", methods=["GET"])
def signin_form():
    return render_template("form.html") 

@app.route("/signin", methods=["POST"])
def signin():
    if request.form["usr"] == "admin" and request.form["pwd"] == "xx":
        return render_template("sign_ok.html", username=request.form["usr"])
    else:
        return render_template("form.html", message="user name or password error", username=request.form["usr"])

if (__name__ == "__main__"):
    app.run()
