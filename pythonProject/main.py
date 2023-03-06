from flask import Flask, render_template, request, redirect, url_for, session


app = Flask(__name__, template_folder='C:/Users/Sathy/Desktop/Live Cinystore/producerdashboard', static_folder='C:/Users/Sathy/Desktop/Live Cinystore/producerdashboard/static')

app.secret_key = 'VX6aLKStjhygC10/4IqOS3fAnRgT9yMOfJ7BBQ+8'


@app.route('/')
def auth_register():
    return render_template('auth_register.html')


@app.route('/dashboard.html')
def dashboard():
    return render_template("Dashboard.html")


@app.route('/auth_login.html')
def auth_login():
    return render_template('auth_login.html')


@app.route('/auth_otp.html')
def auth_otp():
    return render_template('auth_otp.html')


@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/manage-label.html')
def manage_label():
    return render_template("manage-label.html")


@app.route('/create-label.html')
def create_label():
    return render_template('create-label.html')


@app.route('/page1.html')
def page1():
    return render_template("page1.html")


@app.route('/page2.html')
def page2():
    return render_template("page2.html")


@app.route('/page3.html')
def page3():
    return render_template("page3.html")


@app.route('/page4.html')
def page4():
    return render_template("page4.html")


@app.route('/page5.html')
def page5():
    return render_template("page5.html")


@app.route('/page6.html')
def page6():
    return render_template("page6.html")


@app.route('/page7.html')
def page7():
    return render_template("page7.html")


@app.route('/page8.html')
def page8():
    return render_template("page8.html")


@app.route('/profile.html')
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)