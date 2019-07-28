from flask import Flask, request
from twilio import twiml


app = Flask(__name__)


@app.route('/sms', methods=['POST'])
def sms():
    number = request.form['From']
    message_body = request.form.get('Body')
    return message_body

if __name__ == '__main__':
    app.run()
