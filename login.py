from flask import Flask, request, session, Response, url_for, redirect, render_template_string

app = Flask(__name__)
app.secret_key = "secret"  # required for session

# HTML Login Page
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Login Page</title>
</head>
<body>

    <h2>Login Form</h2>

    <form method="POST">
        <input type="text" name="username" placeholder="Enter Username"><br><br>

        <input type="password" name="password" placeholder="Enter Password"><br><br>

        <button type="submit">Login</button>
    </form>

</body>
</html>
"""

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

    return render_template_string(html)


@app.route("/welcome")
def welcome():
    return "Welcome page"


if __name__ == "__main__":
    app.run(debug=True)