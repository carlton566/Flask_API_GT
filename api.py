""" ask: Build a RESTful API with Django and Django REST framework
 
Description:
 
Problem Statement: Create a simple blog application with the following functionalities:
 
User authentication (signup, login, logout).
CRUD operations for blog posts.
Retrieve a list of blog posts with pagination.
Implement proper authentication and authorization for API endpoints. """

from flask import Flask,request,jsonify
import jwt
import os

app=Flask(__name__)



@app.route("/login",methods=["POST"])
def login():
    json_values=request.json
    if json_values["username"]=="Carlton" and json_values["password"]=="1234":
        return {"Response":"Success Login"}
    else:
        return {"Response":"Failed Login"}

@app.route("/create_blog",methods=["POST"])
def create_blog():
    json_values=request.json
    data=file.load("blog.json")
    return {"Response":"Success"}
    
@app.route("/Update_blog",methods=["POST"])
def Update_blog():
    json_value=Request.json
    return {"Response":"Success"}

@app.route("/read_blog",methods=["POST"])
def read_blog():
    list_blog=[
        {
        "Blog1":{
            "name":"DemoBlog1",
            "description":"ABout the demoblog1"
                },
        "Blog2":{
            "name":"DemoBlog2",
            "description":"ABout the demoblog2"
                },
        "Blog3":{
            "name":"DemoBlog3",
            "description":"ABout the demoblog3"
                }
        }
               ]
    return jsonify({"Blog_list":list_blog})

@app.route("/delete_blog",methods=["POST"])
def delete_blog():
    json_value=Request.json
    return {"Response":"Success"}
    


app.run("Localhost",5050)   


