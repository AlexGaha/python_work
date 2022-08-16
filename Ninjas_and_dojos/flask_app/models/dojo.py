# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the dojo table from our database

DATABASE = 'ninjas_and_dojos'

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        
       
    # Now we use class methods to query our database
    
    # ! READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojos with cls.
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    # ! READ/RETRIEVE ONE
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = Dojo(result[0])
        return dojo

    @classmethod
    def get_one_with_ninjas(cls,data):
        query = "SELECT * FROM dojos WHERE ninjas => 1 ;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = result
        return dojo


    # ! CREATE
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s%);"
        return connectToMySQL(DATABASE).query_db(query, data)

    # ! UPDATE
    @classmethod
    def update(cls,data):
        query = "UPDATE dojos SET first_name = %(first_name)s, last_name = %(last_name)s, age = %(age)s, dojo_id = %(dojo_id)s WHERE id = %(id)s ;"
        return connectToMySQL(DATABASE).query_db(query, data)


    # ! DELETE
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM dojos WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

