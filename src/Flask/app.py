import database as db
import json
from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, or_
from functools import wraps
import pymysql
from getPredict import getPredict
from flask_cors import CORS

app = Flask(__name__)
CORS(app, supports_credentials=True)
# local database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:dublinbus@127.0.0.1:3306/test?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.debug = True
db = SQLAlchemy(app)


# Login database
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


# Login functions

def valid_login(username, password):
    user = User.query.filter(and_(User.username == username, User.password == password)).first()
    if user:
        return True
    else:
        return False


def valid_regist(username):
    user = User.query.filter(or_(User.username == username)).first()
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
    validation = 0
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        # return request.data
        if valid_login(result['username'], result['password']):
            # session['username'] = request.form.get('username')
            validation = 1
    return json.dumps({"validation": validation}, ensure_ascii=False)

    # return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/home')


@app.route('/regist', methods=['GET', 'POST'])
def regist():
    error = None
    validation = 0
    if request.method == 'POST':
        result = json.loads(request.data.decode('utf-8'))
        # if result['password1'] != result['password2']:
        #     error = 'The passwords is not same.'
        if valid_regist(result['username']):
            user = User(username=result['username'], password=result['password'])
            db.session.add(user)
            db.session.commit()
            validation = 1
    return json.dumps({"validation": validation}, ensure_ascii=False)


@app.route('/predict', methods=['POST'])
def predict():
    dic = json.loads(request.data.decode('utf-8'))

    result_dict = {}
    for route in dic:
        routeid = route['route_id'].upper()
        oriid = route['ori_id']
        desid = route['des_id']
        dayofweek = route['dayofweek']
        time = route['time']
        pretime = getPredict(routeid, oriid, desid, dayofweek, time)
        result_dict[routeid] = pretime
    return json.dumps(result_dict)


if __name__ == '__main__':
    pymysql.install_as_MySQLdb()
    app.run(host = '0.0.0.0', port = 80)
