from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
time_entries = [] # In-memory storage for simplicity

@app.route('/')
def index():
    return render_template('index.html', entries=time_entries)

@app.route('/punch', methods=['POST'])
def punch():
    action = request.form.get('action')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    time_entries.append({'action': action, 'timestamp': timestamp})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)