from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username.lower().strip() == 'admin' and password.lower().strip() == 'admin':
            return f'Welcome {username}!!'
        elif username.strip() == '' and password.strip() == '':
            return render_template('index.html', inp='Wrong username or password')
        else:
            return render_template('index.html', inp='Wrong username or password')

    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

if __name__ == "__main__":
    app.run(debug=True)
