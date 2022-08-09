from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "hello everyone"


# import statements, maybe some other routes

@app.route('/success')
def success():
    return "success"

@app.route('/hello/<banana>')
def hello_bannana(banana):
    return f"hello{banana}"

# app.run(debug=True) should be the very last statement!
if __name__ == "__main__":
    app.run(debug=True)
