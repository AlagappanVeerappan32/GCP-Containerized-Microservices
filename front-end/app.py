from flask import Flask, render_template, redirect, url_for, request, session
import requests
from forms import RegistrationForm, LoginForm
from flask import flash


app = Flask(__name__)

app.config['SECRET_KEY'] = 'alex'

    

@app.route("/registration", methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':

        # getting registration details
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        location = request.form.get('location')

        payload = {
            'username': username,
            'email': email,
            'password': password,
            'location': location
        }

        response = requests.post('http://localhost:8080/insert_data', json=payload)

        if response.status_code == 200:
            return redirect(url_for('login'))

    reg_form = RegistrationForm()
    return render_template('registration.html',form=reg_form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        # getting login details
        email = request.form.get('email')
        password = request.form.get('password')

        payload = {
            'email': email,
            'password': password
        }

        response = requests.post('http://localhost:3000/get_data', json=payload)

        if response.status_code == 200:
            session['email'] = email
            print("Successful login")
            return redirect(url_for('dashboard'))
        elif response.status_code == 404:
            flash("Email doesn't match", "error")
            print("Email doesn't match")
        elif response.status_code == 401:
            flash("Password doesn't match", "error")
            print("Password doesn't match")
        else:
            if response.status_code != 200:
                flash("Something went wrong!", "error")
            print("Something went wrong")
    
    login_form = LoginForm()
    return render_template('login.html',form=login_form)


@app.route("/logout", methods=['POST'])
def logout():
    if request.method == 'POST':
        email = session.get('email')
        if email:
            print("Email:", email)  # Print the email
            payload = {'email': email}
            response = requests.post('http://localhost:6000/update_data', json=payload)
            if response.status_code == 200:
                session.pop('email')
                return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
        
            
@app.route("/dashboard", methods=['GET', 'POST'])
def dashboard():
    if 'email' not in session:
        flash("Please login to access the dashboard.", "error")
        return redirect(url_for('login'))    
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


