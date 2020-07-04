import database as db
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/lines")
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

if __name__ == '__main__':
    app.run()

