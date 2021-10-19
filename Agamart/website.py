from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = '434731020a30102b273ce9527ce68da8'


@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/course")
def courses():
    return render_template('course.html')


@app.route("/projects")
def projects():
    return render_template('projects.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/dark-mode")
def dark_mode():
    return render_template('home-dark.html')


@app.route("/courses-dark")
def courses_dark():
    return render_template('course-dark.html')


@app.route("/about-dark")
def about_dark():
    return render_template('about-dark.html')


@app.route("/home-dark")
def home_dark():
    return render_template('home-dark.html')


@app.route("/project-dark-dark")
def project_dark():
    return render_template('project-dark.html')


@app.route("/login-dark")
def login_dark():
    return render_template('login-dark.html')


@app.route("/login")
def login():
    return render_template('login.html')


@app.route("/<usr>")
def user(usr):
    return render_template('welcome_page.html', username=usr)


@app.route("/sign_in_dark", methods=["POST", "GET"])
def sign_in_dark():
    if request.method == "POST":
        user_dark = request.form["name_dark"]
        return redirect(url_for("user_dark", usr_dark=user_dark))
    else:
        return render_template('sign_in_dark.html')


@app.route("/sign in", methods=["POST", "GET"])
def sign_in():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template('sign_in.html')


if __name__ == '__main__':
    app.run(debug=True)
