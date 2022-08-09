

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    color = "blue"
    times = 3
    return render_template("index.html", color=color, times=times)
    
@app.route('/play/<int:times>')
def times(times):
    color = "blue"
    times = times
    return render_template("index.html", color=color, times=times)

if __name__=="__main__":
    app.run(debug=True)








