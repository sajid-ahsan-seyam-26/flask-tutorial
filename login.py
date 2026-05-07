# Flask theke Flask, request, session, Response, url_for, redirect, render_template_string import kora hoyeche
from flask import Flask, request, session, Response, url_for, redirect, render_template_string

# Flask app create kora hoyeche
app = Flask(__name__)

# Session use korar jonno secret_key deya hoyeche
app.secret_key = "secret"


# HTML login page ta string er moddhe rakha hoyeche
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>

    <h2>Login Form</h2>

    <!-- Login form create kora hoyeche -->
    <form method="POST">

        <!-- Username input field -->
        <input type="text" name="username" placeholder="Enter Username"><br><br>

        <!-- Password input field -->
        <input type="password" name="password" placeholder="Enter Password"><br><br>

        <!-- Login button -->
        <button type="submit">Login</button>
    </form>

</body>
</html>
"""


# Home route create kora hoyeche, ekhane GET and POST duita method use kora hoyeche
@app.route("/", methods=["GET", "POST"])
def login():

    # User jokhon form submit korbe tokhon POST method kaj korbe
    if request.method == "POST":

        # Form theke username value neya hoyeche
        username = request.form.get("username")

        # Form theke password value neya hoyeche
        password = request.form.get("password")

        # Username admin and password 123 hole login successful hobe
        if username == "admin" and password == "123":

            # Username session er moddhe save kora hoyeche
            session["username"] = username

            # Login successful hole welcome page e redirect korbe
            return redirect(url_for("welcome"))

        # Username ba password wrong hole error message show korbe
        else:
            return Response("invalid credentials. try again", mimetype="text/plain")

    # GET request hole login page show korbe
    return render_template_string(html)


# Welcome route create kora hoyeche
@app.route("/welcome")
def welcome():

    # Welcome page er text return kora hoyeche
    return "Welcome page"


# Ei file direct run korle Flask server start hobe
if __name__ == "__main__":

    # Debug mode on kore app run kora hoyeche
    app.run(debug=True)