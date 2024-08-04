from flask import Flask,json
from flask_mail import *
import logging

app = Flask(__name__)
with open('config.json','r') as f:
        params = json.load(f)['param']




app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = params['gmail-user']
app.config['MAIL_PASSWORD'] = params['gmail-password']
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

logging.basicConfig(level=logging.DEBUG)

@app.route('/mail')
def index_mail():
        msg = Message('Important Mail',
                      sender='vg4041576@gmail.com',
                      recipients=['saurabhdropper@gmail.com'])
        msg.body = "This is to notify you that your course fees is pending"
        mail.send(msg)
        return 'Message sent successfully'

app.run(debug=True)