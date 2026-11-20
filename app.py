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
@app.route("/transfer_money")
def transfer_money():
    return render_template("transfer_money.html")

if __name__ == "__main__":
    app.run()