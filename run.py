"""New cooment i am adding """
from flask import Flask,request,render_template
import pickle
import numpy as np

model = pickle.load(open("lonermodel.pkl","rb"))

app=Flask(__name__)

@app.route("/")
"""home for html file"""
def home():   
    return  render_template("index.html")

@app.route("/",methods=["POST"])
"""Pridiction"""
def pridi():
    
    area_inpute = request.form.get("area")
    area_inpute = float(area_inpute)
    a_inpute = request.form.get("a or b")
    if a_inpute=="a":
        a=1
        b=0
    else:
        a=0
        b=1
        
    output = model.predict(np.array([area_inpute,a,b]).reshape(1,3))
        
    return  render_template("index.html",prediction=output)
    
    

if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080)
    
