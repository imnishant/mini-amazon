from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
#setting secret key
app.secret_key = 'abc'

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
        users = {
            'user1': '123',
            'user2': '1234',
            'user3': '125',
            'user4': '1212'
        }
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            return "User doesn't exist, please go back and try again!"
        if users[username] != password:
            return "Incorrect Password, please go back and try again!"
        session['username'] = username
        return redirect(url_for('home'))
    #it will call home function, now we can change route as we want
    return redirect(url_for('home'))
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

app.run(debug = True)