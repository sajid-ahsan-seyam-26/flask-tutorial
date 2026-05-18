from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/submit", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    """if username == "seyam" and password == "123":
        return render_template("home.html", name=username)
    else:
        return "invalid thik kore koro seyam"""
    valid_users={
        "admin":"123",
        "sagar":"pass",
        "rajat":"raj"

    }
    if username in valid_users and password==valid_users[username]:
        return render_template("homme.html",name=username)
    else:
        return "invalid credentails"

if __name__ == "__main__":
    app.run(debug=True)