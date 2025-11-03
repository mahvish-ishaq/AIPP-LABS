
# -----------------------------------------
# INSECURE demo ONLY: hardcoded secret & credentials.
# Do NOT use in production.
# -----------------------------------------

from flask import Flask, request, session, redirect, url_for

app = Flask(__name__)

# ===== INSECURE: hardcoded secret (for demo only) =====
app.secret_key = 'supersecret'  
USERS = {
    "admin": "password123",
    "user": "userpass"
}

@app.route('/')
def home():
    if 'user' in session:
        return f"Welcome {session['user']}! <br><a href='/logout'>Logout</a>"
    return '''
        <h2>Insecure Demo Login</h2>
        <form method="POST" action="/login">
            Username: <input name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username', '')
    password = request.form.get('password', '')

    # INSECURE direct comparison with hardcoded store
    if username in USERS and USERS[username] == password:
        session['user'] = username
        return redirect(url_for('home'))
    return "Invalid credentials. <a href='/'>Try again</a>", 401

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    # Debug off to match your earlier run message; run locally only.
    app.run(debug=False)
