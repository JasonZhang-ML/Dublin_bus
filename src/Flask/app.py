import database as db
#from Externel_Data_API import bus_weather_crawler as API
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from functools import wraps
import pymysql



app = Flask(__name__)
#local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kki880611@127.0.0.1:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

#Login database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % self.username

# database
@app.before_first_request
def create_db():
    db.drop_all()
    db.create_all()
    
    admin = User(username='admin', password='123', email='admin@example.com')
    db.session.add(admin)

    guestes = [User(username='ywq', password='123', email='ywq@example.com'),
               User(username='guest', password='guest', email='guest@example.com')]
    db.session.add_all(guestes)
    db.session.commit()

#Login functions

def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password)).first()
    if user:
        return True
    else:
        return False

def valid_regist(username, email):
    user = User.query.filter(or_(User.username == username, User.email == email)).first()
    if user:
        return False
    else:
        return True

# route


@app.route('/')
@app.route('/home')
def index():
    return render_template("index.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            #session['username'] = request.form.get('username')
            return redirect('/home')
        else:
            error = 'wrong username or password!'

    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/home')

@app.route('/regist', methods=['GET','POST'])
def regist():
    error = None
    if request.method == 'POST':
        if request.form['password1'] != request.form['password2']:
            error = 'The passwords is not same.'
        elif valid_regist(request.form['username'], request.form['email']):
            user = User(username=request.form['username'], password=request.form['password1'], email=request.form['email'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            error = 'The username or email has been registed!'
    
    return render_template('regist.html', error=error)

@app.route('/lines')
def linesInfo():
    return db.get_line_ids()

@app.route('/direction', methods=['POST'])
def direction():
    #may be we need to build direction function?
    pass

@app.route('/predict', methods=['POST'])
def predict():
    req = {}
    req['orig_stop_id']=request.form['origin'].split(', ')[0]
    req['dest_stop_id'] = request.form['destination'].split(', ')[0]
    #get prediction from model
    return 0

@app.route('/weather', methods=['POST'])
def weather():
    crawler = API.BusWeatherCrawler()
    result = crawler.request_weather_api(53.2989008333,-6.1959722222)
    rDict = {"main": result['weather'][0]['main'], "temp": result['main']['temp']}
    j = json.dump(rDict)
    return j

if __name__ == '__main__':
    #print(weather())
    pymysql.install_as_MySQLdb()
    app.run()

