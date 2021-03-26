from flask import Flask
from flask import url_for
from flask import render_template
from flask import request
from data import db_session

app = Flask(__name__)


@app.route('/avareya_dostup', methods=['POST', 'GET'])
def avareya_dostup():
    if request.method == 'GET':
        param = {}
        return render_template('base.html', **param)
    elif request.method == 'POST':
        print(request.form['id1'])
        print(request.form['id2'])
        print(request.form['password1'])
        print(request.form['password2'])
        return "Запрос отправлен. Ждите..."


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("index.html", news=news)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')