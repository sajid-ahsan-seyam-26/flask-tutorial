from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    valid_users = {
        "admin": "123",
        "sagar": "pass",
        "rajat": "raj"
    }

    if username in valid_users and password == valid_users[username]:
        return redirect(url_for("portfolio", name=username))
    else:
        return render_template("home.html", error="Invalid username or password")

@app.route("/portfolio")
def portfolio():
    name = request.args.get("name", "User")
    return render_template("portfolio.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)