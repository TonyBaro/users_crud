from mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def retrieve(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_schema').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def add_user(cls,data):
        query="INSERT INTO users(first_name,last_name,email) VALUES (%(fname)s,%(lname)s,%(email)s)"
        return connectToMySQL('users_schema').query_db( query, data )

    @classmethod
    def del_user(cls,data):
        query="DELETE FROM users WHERE id =%(id)s"
        return connectToMySQL('users_schema').query_db( query, data )
    
    @classmethod
    def retrieve_user(cls,data):
        query = "SELECT * FROM users WHERE id=%(idnum)s;"
        user = connectToMySQL('users_schema').query_db(query, data)
        return user