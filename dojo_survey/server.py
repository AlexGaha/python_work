from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['post'])
def handle_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    return redirect('/result')

@app.route('/result')
def result():
    print(session)
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True)