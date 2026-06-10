from flask import (
    Flask,
    render_template,
    session,
    redirect,
    url_for,
    request
)

from face_module.login_face import authenticate_face
from face_module.register_face import register_face

app = Flask(__name__)
app.secret_key = "face_login_secret_key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/face-register", methods=["POST"])
def face_register():

    username = request.form["username"]

    success = register_face(username)

    if success:
        return redirect(
            url_for("login")
        )

    return redirect(
        url_for("register")
    )


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

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect(url_for("home"))

@app.route("/face-login", methods=["POST"])
def face_login():

    username = authenticate_face()

    if username:

        session["user"] = username

        return redirect(
            url_for("dashboard")
        )

    return redirect(
        url_for("login")
    )


if __name__ == "__main__":
    app.run(debug=True)