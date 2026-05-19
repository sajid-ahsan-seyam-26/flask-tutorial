from flask import Flask, render_template, request

app = Flask(__name__)         # flask kon file theke app toiri korche

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
        return render_template("home.html", name=username, success=True)
    else:
        return render_template("home.html", error="Invalid username or password")

if __name__ == "__main__":
    app.run(debug=True)
