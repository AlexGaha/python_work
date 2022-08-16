from flask_app import app , render_template, request, redirect
from flask_app.models.user import User


@app.route('/users/new')
def form():
    return render_template("create.html")

#creating a key for session
# creating route for home page
@app.route('/users/new', methods=['post'])
def new_user():
    print(request.form)
    User.save(request.form)
    return redirect('/users')  

    #new_user = User.save(data)
    #print(new_user)
    #return redirect('/users')

#DELETE

@app.route('/delete/<int:id>')
def delete_user(id):
    User.destroy({'id': id})
    return redirect(f"/")

#EDIT

@app.route('/edit/<int:id>')
def edit_user(id):
    data = {'id':id}
    return render_template('edit_user.html', user = User.get_one(data))

#UPDATE USER
@app.route('/update/user', methods = ['post'])
def update_user():
    print (request.form)
    User.update(request.form)
    return redirect('/users/new')

    
#ROUTE FOR DISPLAYING USERS(DASHBOARD)
@app.route('/users')
def users():
    # GET ALL USERS FROM THE DB
    info = User.get_all()
    print(info)
    # PASS THE ALL USERS TO THE HTML
    return render_template('Read(All).html', users=info)


