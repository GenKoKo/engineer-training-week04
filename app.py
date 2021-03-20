from flask import Flask,request,redirect,render_template, session,url_for
import json


app = Flask(__name__,
            static_folder="static",
            static_url_path="/"
        )

app.secret_key = '_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def index():
    return render_template("/index.html")


@app.route("/member", methods = ["GET","POST"])
def member():
    if "ac" in session and request.method == "POST":
        return render_template("/member.html")
    elif "ac" in session and request.method == "GET":
        print("direct member page test success")
        print(session)
        return render_template("/member.html")
    
    elif not "ac" in session and request.method == "GET":
        print("status: no login")
        print(session)
        return redirect(url_for("index"))


@app.route("/signin", methods =["POST"])
def signin():

    if request.form["a"] == "test" and request.form["p"] == "test":
        session["ac"] = request.form["a"]
        session["pa"] = request.form["p"]
        print("status: log in")
        print(session)
        return redirect(url_for("member"))

    elif request.form["a"] != "test" or request.form["p"] != "test":
        print("status: login fail")
        print(session)
        return redirect(url_for("error"))

    # 這會造成 未登錄狀況，直接landing member page → 產生bad request 原因未明 
    # elif request.method == "GET" and session["ac"] == "test" and session["pa"] == "test":
    #     print("member test success")
    #     return render_template("/member.html")


    else:
        print(session)
        print("status: login fail")
        return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("/error.html")

@app.route("/signout")
def signout():
    session.pop("ac",None)
    session.pop("pa", None)
    print("status: log out")
    print(session)
    return redirect(url_for("index"))


app.run(port=3000)