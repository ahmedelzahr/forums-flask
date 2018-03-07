
from flask import render_template,request,redirect ,url_for
from app import models
from app import app, member_store, post_store
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

@app.route("/tobic/delete/<id>")
def topic_delete(id):
    post_store.delete(int(id))
    print id
    return redirect(url_for("home"))

@app.route("/tobic/edit/<id>", methods = ["GET", "POST"])  
def topic_edit(id):
    if request.method == "POST":
    	post=post_store.get_by_id(int(id))
        post.title = request.form["title"]
        post.subject=request.form["content"]
        post_store.update(post)
        return redirect(url_for("home"))

    else:
        return render_template("topic_edit.html",po=post_store.get_by_id(int(id)))

@app.route("/tobic/show/<id>", methods = ["GET", "POST"])  
def topic_show(id):
    if request.method == "POST":
    	print "back"
        return redirect(url_for("home"))

    else:
        return render_template("topic_show.html",po=post_store.get_by_id(int(id)))        
