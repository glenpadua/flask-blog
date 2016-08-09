from flask import render_template, flash, redirect
from app import app
from forms import LoginForm

@app.route("/")
@app.route("/index")

def index():
    user ={"name" : "Glen"} # fake user
    posts = [   # fake array of posts
            {
                "author" : {"name" : "John"},
                "body" : "Beautiful day in Kochi!"
            },
            {
                "author" : {"name" : "Glen"},
                "body" : "Suicide Squad FTW!"
            }
    ]
    return render_template("index.html",
                                            title = "Home",
                                            user = user,
                                            posts = posts)


@app.route("/login", methods = ["GET", "POST"])

def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash("Login requested for Open ID='%s', remember_me=%s" %
              (form.open_id.data, str(form.remember_me.data)))
        return redirect("/index")
    return render_template("login.html",
                                            title = "Sign In",
                                            form = form)




