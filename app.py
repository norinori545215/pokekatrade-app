
from flask import Flask, render_template, request, redirect, session
import csv
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'default-secret')

def load_invites():
    with open('data/invites.csv', newline='') as f:
        return [row[0] for row in csv.reader(f)]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        code = request.form.get('code')
        if code in load_invites():
            session['user'] = code
            return redirect('/dashboard')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html')

@app.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if 'user' not in session:
        return redirect('/')
    if request.method == 'POST':
        with open('data/feedback.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([session['user'], request.form.get('feedback'), request.form.get('rating')])
        return redirect('/dashboard')
    return render_template('feedback.html')

@app.route('/admin')
def admin():
    feedback = []
    if os.path.exists('data/feedback.csv'):
        with open('data/feedback.csv', newline='') as f:
            reader = csv.reader(f)
            next(reader)
            feedback = list(reader)
    invites = []
    if os.path.exists('data/invites.csv'):
        with open('data/invites.csv', newline='') as f:
            invites = [row[0] for row in csv.reader(f)]
    return render_template('admin.html', feedback=feedback, invites=invites)

if __name__ == '__main__':
    app.run(debug=True)
