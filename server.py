from flask import Flask, redirect
from flask import render_template,request
from datetime import datetime
import sqlite3
app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def home():
    current_year=datetime.now().year
    return render_template("portfolio.html",year=current_year)


#
@app.route('/#contact',methods=['GET', 'POST'])
def receive_data():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    return redirect(request.referrer)


# @app.route("/form-entry", methods=["POST"])
# def receive_data():
#     data = request.form
#     print(data["name"])
#     print(data["email"])
#     print(data["phone"])
#     print(data["message"])
#     return "<h1>Successfully sent your message</h1>"

# @app.route('/#work')
# def home():
#     current_year=datetime.now().year
#     return render_template("portfolio.html",year=current_year)
if __name__ == "__main__":
    app.run(debug=True)


# db = sqlite3.connect("portfolio")
# cursor = db.cursor()