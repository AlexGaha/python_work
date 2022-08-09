from contextlib import redirect_stderr
from distutils.log import debug
from flask import Flask, render_template,request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret' 

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/up')
def up():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')

#@app.route('/')
#def destroy():


    

if  __name__ == "__main__":
    app.run(debug=True)