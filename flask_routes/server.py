from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/Dojo')
def dojo():
    return "Dojo"

@app.route('/say/<michael>')
def say (michael):
    print(michael)
    return "say, " + michael

@app.route('/repeat/<int:num>/<dogs>') 
def repeat( num,dogs):
    return f"Hello  {dogs * num}" 



if __name__ == "__main__":
    app.run(debug=True)
