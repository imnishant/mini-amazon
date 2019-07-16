from flask import Flask, render_template, request, redirect, url_for, session
from model.model import save_user, user_exists, RegistrationForm, add_product, product_exists, products_list

app = Flask(__name__)
#setting secret key
app.secret_key = 'abc'
form = RegistrationForm()
@app.route('/')
def home():
    return render_template('home.html',page = "home")

@app.route('/about')
def about():
    return render_template('about.html',page = "about")

@app.route('/contact')
def contact():
    return render_template('contact.html',page = "contact")

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        result = user_exists(username)
        if result == None:
            return "User doesn't exist, please go back and try again!"
        elif result['password'] != password:
            return "Incorrect Password, please go back and try again!"
        
        session['username'] = username
        session['c_type'] = result['c_type']
        return redirect(url_for('home'))
    #it will call home function, now we can change route as we want
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

@app.route('/products',methods=['GET','POST'])
def products():
    if request.method == 'POST':
        product_info = {}
        product_info['name'] = request.form['name']
        product_info['price'] = request.form['price']
        product_info['description'] = request.form['description']
        product_info['seller'] = session['username']
        
        if product_exists(product_info['name']):
            return "Product Already Exists"
        add_product(product_info)
        return "Product added! Check your DB"
    return render_template('products.html', products = products_list())
@app.route('/register')
def register():
    return redirect(url_for('register'))

@app.route('/signup', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        
        user_info = {}
        
        user_info['username'] = request.form['username']
        user_info['password'] = request.form['password1']
        password2 = request.form['password2']
        user_info['c_type'] = request.form['type']
        
        if user_info['c_type'] == 'buyer':
            user_info['cart'] = {}
        if user_exists(user_info['username']):
            return "Username already exists"
        if user_info['password'] != password2:
            return "Password doesn't match"
        
        save_user(user_info)
        return redirect(url_for('home'))
    return render_template('register.html')
    """
    
    form = RegistrationForm(request.POST)
    
    if request.method == 'POST':
        user_info = {}
        user_info['username'] = form.username.data
        user_info['password'] = form.password1.data
        password2 = form.password2.data
        user_info['c_type'] = form.c_type.data
        
        if user_info['c_type'] == 'buyer':
            user_info['cart'] = {}
        if user_exists(user_info['username']):
            return "Username already exists"
        if user_info['password'] != password2:
            return "Password doesn't match"
        save_user(user_info)
        return render_template('home', form = form) 
    return redirect(url_for('home'))"""
app.run(debug = True)