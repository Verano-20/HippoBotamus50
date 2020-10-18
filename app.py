from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from instapy import InstaPy

# Configure app
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

#Log in to HippoBOTamus insta
'''
 Details not included for public repo,see youtube
 demo in readme or enter your own details to test.
'''
username = "hippobotamus50"
password = "password50"

session=InstaPy(username=username, password=password, headless_browser=True)
session.login()
session.like_by_tags(["cs50"], amount=-9)


@app.route("/")
def index():
    #Show Homepage
    return render_template("index.html")


@app.route("/follow" , methods=["GET", "POST"])
def instagram():
    #Show follow page
    if request.method == "POST":
        #Follow the handle submitted

        #Get sumbitted handle
        handle=request.form.get("handle")
        if not handle:
            return render_template('follow.html')

        #Check the handle doesn't start with "@"
        if handle[0] == "@":
            #Drop first char
            handle=handle[1:]

        #Put handle into a list to feed into the follow function.
        accounts=[handle]

        #Follow handle
        session.follow_by_list(accounts, times=10, interact=False)

        #Check if user has been followed by getting following of HippoBOTamus
        HippoBOTamus_following = session.grab_following(username="HippoBotamus50", amount="full", live_match=True)

        if not handle in HippoBOTamus_following:
            #Return error
            render_template("cantfollow.html", handle=handle)
        
        return render_template("followed.html", handle=handle)

    else:
        return render_template("follow.html")
    

@app.route("/following" , methods=["GET", "POST"])
def following():
    #Show following page
    if request.method == "POST":
        #Get handle from user input
        handle=request.form.get("handle")

        if not handle:
            return render_template('following.html')

        #Check the handle doesn't start with "@"
        if handle[0] == "@":
            #Drop first char
            handle=handle[1:]

        #Get following for this handle
        handles=session.grab_following(username=handle, amount="full", live_match=True)

        return render_template("following.html", handles=handles, handle=handle)

    else:
        #Show all handles HippoBOTamus is following
        handle="HippoBotamus50"
        handles=session.grab_following(username="HippoBotamus50", amount="full", live_match=True)

        return render_template("following.html", handles=handles, handle=handle)


@app.route("/unfollow" , methods=["GET", "POST"])
def unfollow():
    #Get page for HippoBOTamus to unfollow a handle
    if request.method == "POST":
        #Get handle
        handle=request.form.get("handle")

        if not handle:
            return render_template('unfollow.html')

        #Check the handle doesn't start with "@"
        if handle[0] == "@":
            #Drop first char
            handle=handle[1:]

        #Put handle into list to feed into unfollow function
        handles=[handle]

        #Unfollow user
        session.unfollow_users(amount=1, custom_list_enabled=True, custom_list=handles, custom_list_param="all", style="FIFO")

        return render_template("unfollowed.html", handle=handle)

    else:
        #Show unfollow page
        return render_template("unfollow.html")