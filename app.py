from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for
)

app = Flask(__name__)
app.secret_key = "face_login_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "user" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["user"]
    )


@app.route("/test-login")
def test_login():

    session["user"] = "Arya"

    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)