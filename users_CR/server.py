from flask import Flask, render_template, request, redirect
# import the class from friend.py

from user import User
app = Flask(__name__)

# ROUTE FOR DISPLAYING A FORM
@app.route('/users/new')
def form():
    return render_template("create.html")

#creating a key for session
# creating route for home page
@app.route('/users/new', methods=['post'])
def new():
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],

    }   

    new_user = User.save(data)
    print(new_user)
    return redirect('/users')

    
#ROUTE FOR DISPLAYING USERS(DASHBOARD)
@app.route('/users')
def users():
    # GET ALL USERS FROM THE DB
    info = User.get_all()
    print(info)
    # PASS THE ALL USERS TO THE HTML
    return render_template("Read(All).html", users=info)




if __name__ == "__main__":
    app.run(debug=True)
    






