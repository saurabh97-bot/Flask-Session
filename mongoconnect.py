from flask import Flask,json,request,render_template,redirect,url_for
from pymongo import MongoClient

app = Flask(__name__)

mongo_uri = "mongodb+srv://vg4041576:hDHxc0ii45Ji5CWi@flaskcluster.apei14w.mongodb.net/?retryWrites=true&w=majority&appName=FlaskCluster"
client = MongoClient(mongo_uri)

db = client['Session-DB']
collection = db['TestUser']
collection1 = db['FormData']

@app.route('/test',methods=['POST'])
def test_data():
    data = request.json
    collection.insert_one(data)
    return 'Data has been sent successfully...!!!'

@app.route('/form')
def index():
    return render_template('form.html')

@app.route('/submit',methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        city = request.form['city']
        address = request.form['address']
        form_data = {
            'name':name,
            'age':age,
            'city':city,
            'address':address
        }
        collection1.insert_one(form_data)
        return 'Your Form has been submitted successfully'
    return redirect(url_for('index'))

app.run(debug=True)
