from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def main():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%I:%M %p")
    
    return "<center><h1>Current Time: " + current_time + "</h1></center>" # really want to use CSS for alignment


