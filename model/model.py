from pymongo import MongoClient
from wtforms import Form, BooleanField, StringField, validators, RadioField
client = MongoClient()
db = client['amazon']   #It's same as use dbname in mongo shell

class RegistrationForm(Form):
    username     = StringField('Username', [validators.Length(min=4, max=25)])
    password1     = StringField('Password1', [validators.Length(min=6, max=35)])
    password2     = StringField('Password2', [validators.Length(min=6, max=35)])
    c_type = RadioField('Type')
    

def user_exists(username):
    query = {'username':username}
    result = db['users'].find_one(query)
    return result
def save_user(user_info):
    db['users'].insert_one(user_info)
    
def product_exists(product_name):
    query = {'name': product_name}
    result = db['products'].find_one(query)
    return result

def add_product(product_info):
    db['products'].insert_one(product_info)
    
def products_list():
    
    if session['c_type'] == 'buyer':
        result = db['products'].find({})
        return result
    query = {"seller": session['username']}
    result = db['products'].find(query)
    return result
    