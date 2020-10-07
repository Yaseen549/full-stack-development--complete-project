from flask import Flask, render_template, request, session, redirect, url_for, g
import model

app = Flask(__name__)
app.secret_key = 'jumpjacks'

username = ''
adminusername = ''

user = model.check_users()
admin = model.check_admin()

# User Login
@app.route('/', methods = ['GET'])
def home():
    if 'username' in session:
        g.user = session['username']
        return render_template('football.html', message = "Welcome " + session['username'])
    elif 'adminusername' in session:
        g.admin = session['adminusername']
        return render_template('admindashboard.html', message = "welcome " + session['adminusername'])
    return render_template('homepage.html', message = "Login! or Sign Up!")

#admin login
# @app.route('/adminhome', methods = ['GET'])
# def adminhome():
#     if 'username' in session:
#         g.admin = session['username']
#         return render_template('admindashboard.html', message = "welcome " + session['username'])
#     return render_template('adminlogin.html', message = "Login! or Sign Up!")


@app.route('/login', methods = ['GET','POST'])

def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = request.form['username']
        pwd = model.check_pw(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('home'))
        else:
            return render_template('index.html', message = "Incorrect Password!")
    return render_template('index.html')


@app.route('/adminlogin', methods = ['GET','POST'])
def adminlogin():
    if request.method == 'POST':
        session.pop('adminusername', None)
        areyouadmin = request.form['adminusername']
        pwd = model.check_admin_pw(areyouadmin)
        if request.form['adminpassword'] == pwd:
            session['adminusername'] = request.form['adminusername']
            return redirect(url_for('home'))
        else:
            return render_template('adminlogin.html', message = "Incorrect Password!")
    return render_template('adminlogin.html')


@app.before_request

def before_request():
    g.username = None
    g.adminusername = None
    if 'username' in session:
        g.username = session['username']
    elif 'adminusername' in session:
        g.adminusername = session['adminusername']


@app.route('/signup',methods = ['GET','POST'])

def signup():
    if request.method == 'GET':
        return render_template('signup.html', message = " ")
    else:
        username = request.form['username']
        password = request.form['password']
        fav_color = request.form['fav_color']
        message = model.signup(username,password,fav_color)
        return render_template('signup.html', message = message)



@app.route('/update',methods = ['GET','POST'])

def update():
    if request.method == 'GET':
        return render_template('football.html', message = "Updated")
    else:
        username = request.form['username']
        password = request.form['password']
        fav_color = request.form['fav_color']
        message = model.update(username,password,fav_color)
        return render_template('football.html', message = message)



@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    elif 'adminusername' in session:
        return session['username']
    return redirect(url_for('login'))




@app.route('/logout')
def logout():
    if 'username' in session:
        session.pop('username', None)
    elif 'adminusername' in session:
        session.pop('adminusername', None)
    return redirect(url_for('home'))




@app.route('/termsofus', methods = ['GET'])

def terms_of_use():
    return render_template('termsofus.html')


@app.route('/privacy', methods = ['GET'])

def privacy():
    return render_template('privacy.html')


@app.route('/aboutus', methods = ['GET'])

def about_us():
    return render_template('aboutus.html')



@app.route('/display_users')
def displayusers():
    data = model.display_users()
    return render_template("admindashboard.html", data=data)



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 7000, debug = True)
