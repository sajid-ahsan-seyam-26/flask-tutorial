from flask import Flask,request
#flask libarary import korbe

app = Flask(__name__)                #ekhane flask application toiri kora hocce

@app.route("/")                      #/ holo ekta decoder jeta root e niye jabe
def home():
    return "hello user"
@app.route("/about")                #about page e niye jabe
def about():
    return "this is about page"
@app.route("/contact")             #contact page e niye jabe
def contact():
    return "this is contact"
@app.route("/submit", methods=["GET", "POST"]) # ei route allow kore get and post request

def submit():                                  # function name submit                                           #request ta post kina seta check kore
    if request.method=="POST":                 #retuen this request for post method
        return "you send data"


if __name__ == "__main__":
    app.run(debug=True)