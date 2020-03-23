	# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 16:54:35 2020

@author: Hp
"""

from flask import Flask,render_template
app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8001,debug=True)
