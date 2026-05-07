from flask import Flask, request, session, Response, url_for, redirect

app = Flask(__name__)
app.secret_key = "secret"  # required for session

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username == "admin" and password == "123":
            session["username"] = username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid credentials. try again", mimetype="text/plain")

    return "Login Page"

@app.route("/welcome")
def welcome():
    return "Welcome page"

if __name__ == "__main__":
    app.run(debug=True)