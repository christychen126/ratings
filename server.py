"""Movie Ratings."""

from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, User, Rating, Movie


app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Normally, if you use an undefined variable in Jinja2, it fails
# silently. This is horrible. Fix this so that, instead, it raises an
# error.
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    # a = jsonify([1,3])
    # return a
    return render_template("homepage.html")


@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

@app.route("/register", methods=['GET'])
def register_form():
    """takes user to registration form"""

    return render_template("register_form.html")

@app.route("/register", methods=['POST'])
def register_process():
    """process the registration"""


    input_email = request.form.get("user")
    input_password = request.form.get("password")

    check_user = db.session.query(User).filter_by(email=input_email).first()

    
    if check_user: 
        print "You are already registered!"

    else:
        new_user = User(email=input_email, password=input_password)

        print "hey y'all"
        #replace with flash msg

        db.session.add(new_user)
        db.session.commit()
       

    #check if user email in database
    #if not, write email and password into db

    return redirect("/")

@app.route("/login", methods=['POST'])    
def login():
    """processes user login and redirects user to homepage after login"""


    #create sesion
    #validate username matches password, add user to session by id 
    #flash message in base.html


    return redirect("/")

@app.route("/logout", methods=['POST'])    
def logout():
    """log user out and redirects user to homepage after logout"""
    # delete user from session


    return redirect("/")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)


    
    app.run(port=5000)
