import models
import store
import dummy_data
from flask import render_template,request,redirect ,url_for
from app import app
post_store=store.PostStore()
member_store=store.MemberStore()
dummy_data.seed_stores(member_store, post_store)
@app.route("/")
def home():
    return render_template("index.html",posts=post_store.get_all())
@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")