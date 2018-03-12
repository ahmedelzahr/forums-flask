from flask import Flask
from app import models,store,dummy_data
app=Flask(__name__)
post_store=store.PostStore()
member_store=store.MemberStore()
dummy_data.seed_stores(member_store, post_store)
from app import views 
from app import api  
