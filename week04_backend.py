from flask import Flask
from flask import request
app = Flask(__name__,
            static_folder="static",
            static_url_path="/"
        )


@app.route("/")
def index():
    # print("Method: ", request.method)
    # print("protocal: ", request.scheme)
    print("browser and OS: ", request.headers.get("user-agent"))
    print("Lang: ", request.headers.get("accept-language"))
    print("URL", request.headers.get("referrer"))
    
    lang=request.headers.get("accept-language")
    if lang.startswith("en"):
        return "Hello Week04"
    else:
        return "哈囉 Week04"

@app.route("/getData")
def getData():
    return "No Data"

@app.route("/user/<name>")
def user(name):
    return "Hello "+name

app.run(port=3000)