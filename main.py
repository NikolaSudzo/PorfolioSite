from flask import Flask, render_template, send_file, request, flash, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("PORTFOLIO")


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/download')
def download():
    path = 'static/assets/CV.pdf'
    return send_file(path, as_attachment=True)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        res = pd.DataFrame({'name': name, 'email': email, 'message': message}, index=[0])
        print(res.to_csv())
        flash("Your message was successfully sent")
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
