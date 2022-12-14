from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes

# import statements, maybe some other routes
    
@app.route('/')
def index():
    return render_template('index.html')
    
# app.run(debug=True) should be the very last statement! 



@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    # Here we add two properties to session to store the name and email
    session['username'] = request.form['name']
    session['useremail'] = request.form['email']
    return redirect('/show')

@app.route('/show')
def show_user():
    return render_template('index.html', name_on_template=session['username'], email_on_template=session['useremail'])



if __name__ == "__main__":
    app.run(debug=True)