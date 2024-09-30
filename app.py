from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np

model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key="AIzaSyCotr34E5ke8YHUcMAs6hvWfQ09R4SKt2Y")

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
    q = request.form.get("q")
    return(render_template("main.html",r=q))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
    return(render_template("makersuite.html"))

@app.route("/makersuite_1",methods=["GET","POST"])
def makersuite_1():
    q = "Can you help me prepare my tax return?"
    r = model.generate_content(q)
    return(render_template("makersuite_1_reply.html",r=r.text))

@app.route("/makersuite_gen",methods=["GET","POST"])
def makersuite_gen():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("makersuite_gen_reply.html",r=r.text))

if __name__ == "__main__":
    app.run()
