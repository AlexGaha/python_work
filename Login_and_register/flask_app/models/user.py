
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
from flask_app import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

DATABASE = 'users'
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.dojo = data['dojo']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # ... other class methods
    # class method to save users to the database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db( query )

        users = []
        for user in results:
            users.append( cls(user))
        return users
    #CREATE
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users ( first_name , last_name , email, password ) VALUES ( %(first_name)s , %(last_name)s , %(email)s ,%(password)s );"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL(DATABASE).query_db( query, data )
    #READ/RETRIEVE ONE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s ;"
        result = connectToMySQL(DATABASE).query_db( query, data )
        user = User(result[0])
        return user
    # VALIDATING EMAIL
    @classmethod
    def get_one_with_email(cls,data) -> object or bool:
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        print(result)
        if len(result) < 1:
            return False
        else:
            user = User(result[0])
        return user
        
    


    # Static methods don't have self or cls passed into the parameters.
    # We do need to take in a parameter to represent our burger
    @staticmethod
    def validate_user(user) -> bool:
        is_valid = True
        if len(user['first_name']) < 3:
            is_valid = False
            flash("Name must be at least 3 chars", 'first_name')
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!", 'email')
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("passwords must match!", 'password')
            is_valid = False
        return is_valid
    