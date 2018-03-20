from flask import render_template,request,redirect ,url_for,jsonify,abort
from app import models
from app import app, member_store, post_store
#-----------------------------------------------------------------------

@app.route("/api/topic/all")
def topic_get_all():
    posts=[post.as_dict() for post in post_store.get_all()]
    return jsonify(posts)
#-----------------------------------------------------------------------

@app.route("/api/topic/add",methods=["POST"])
def topic_create():
    request_data=request.get_json()
    new_post=models.Post(title=request_data["title"],content=request_data["content"])
    post_store.add(new_post)
    return jsonify(new_post.__dict__)
#-----------------------------------------------------------------------

@app.route("/api/topic/edit/<int:id>" , methods = [ "PUT"] )
def topic_modrfy(id):
    post = post_store.get_by_id(id)
    request_data=request.get_json()
    if post is None:
        abort(404,"this id is not exist")
    if request.method == "POST":
        post.title = request_data["title"]
        post.topic = request_data["content"]
        post_store.update(post)
        return jsonify(post.__dict__)
#-----------------------------------------------------------------------

@app.route("/api/topic/delete/<int:id>", methods=['DELETE'])
def topic_remove(id):
    try:
    	post = post_store.get_by_id(id)
    	post_store.delete(id)
    except ValueError:	
        abort(400,"this id not found")
    return jsonify(post.as_dict())    
    
#-----------------------------------------------------------------------

@app.route("/api/topic/show/<int:id>",methods=['GET'])  
def topic_view(id):
    post = post_store.get_by_id(id)
    if post is None:
        abort(404,"this id is not exist")
    return jsonify(post.as_dict())        
#-----------------------------------------------------------------------
    
@app.errorhandler(400)
def bad_request(error):
    return jsonify(message = error.description)        
