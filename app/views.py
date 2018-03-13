
from flask import render_template,request,redirect ,url_for,jsonify,abort
from app import models
from app import app, member_store, post_store
#-----------------------------------------------------------------------
@app.route("/")
def home():
    return render_template("index.html",posts=post_store.get_all())
#-----------------------------------------------------------------------
@app.route("/topic/add", methods = ["GET", "POST"])
def topic_add():
    if request.method == "POST":
        new_post = models.Post(request.form["title"], request.form["content"])
        post_store.add(new_post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_add.html")
#-----------------------------------------------------------------------
@app.route("/tobic/delete/<int:id>")
def topic_delete(id):
    try:
        post_store.delete(id)
    except ValueError:
        abort(404,"this id not found")

    return redirect(url_for("home"))
#-----------------------------------------------------------------------
@app.route("/topic/edit/<int:id>" , methods = ["GET", "POST"] )
def topic_edit(id):
    if post is None:
        abort(404,"this id is not exist")

    if request.method == "POST":
        post = post_store.get_by_id(id)
        post.title = request.form["title"]
        post.topic = request.form["content"]
        post_store.update(post)
        return redirect(url_for("home"))
    else:
        post = post_store.get_by_id(id)
        return render_template("topic_edit.html", post=post)
#-----------------------------------------------------------------------
@app.route("/tobic/show/<int:id>", methods = ["GET", "POST"])  
def topic_show(id):
    post=post_store.get_by_id(id)
    if post is None:
        abort(404,"this id is not exist")
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return render_template("topic_show.html",po=post)
#-----------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',message=error.description)
