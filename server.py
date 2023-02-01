from dotenv import load_dotenv
from flask import Flask, flash, redirect, render_template, request, url_for
import vonage

from os import environ as env

# Load environment variables from a .env file:
load_dotenv('.env')

# Load in configuration from environment variables:
VONAGE_API_KEY = env['VONAGE_API_KEY']
VONAGE_API_SECRET = env['VONAGE_API_SECRET']
VONAGE_NUMBER = env['VONAGE_NUMBER']

# Create a new Vonage Client object:
client = vonage.Client(
    key=VONAGE_API_KEY, secret=VONAGE_API_SECRET
)

# Initialize Flask:
app = Flask(__name__)
app.config['SECRET_KEY'] = env['FLASK_SECRET_KEY']

@app.route('/')
def index():
    """ A view that renders the Send SMS form. """
    return render_template('index.html')

@app.route('/send_sms', methods=['POST'])
def send_sms():
    """ A POST endpoint that sends an SMS. """
 
    # Extract the form values:
    to_number = request.form['to_number']
    message = request.form['message']
 
    # Send the SMS message:
    result = client.sms.send_message({
        'from': VONAGE_NUMBER,
        'to': to_number,
        'text': message,
    })
 
    # Redirect the user back to the form:
    return redirect(url_for('index'))