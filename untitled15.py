# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:52:28 2020

@author: ab
"""

from flask import Flask, render_template, request

app=Flask(__name__)


@app.route('/',methods=['GET','POST'])
def my_form():
    
      if request.method == 'POST':
                 
          user = request.form['nm']
          user1 = request.form['nm1']
          
          user3=[user,user1]
          with open("n.txt",'w+') as f:
             for i in user3 :
               f.write(i)
               f.write("\n")
               

      return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)