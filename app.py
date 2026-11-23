# blockchain application

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET", "POST"])
def main():
    r = request.form.get("q", "")
    return render_template("main.html", r=r)

@app.route("/transferMoney", methods=["GET", "POST"])
def transferMoney():
    return render_template("transferMoney.html")

@app.route("/storeMoney", methods=["GET", "POST"])
def storeMoney():
    return render_template("storeMoney.html")

if __name__ == "__main__":
    app.run()