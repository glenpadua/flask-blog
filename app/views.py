from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

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
