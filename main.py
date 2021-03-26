from flask import Flask
from data import db_session
from data.Users import User
from data.Jobs import Jobs
import datetime
from flask import url_for
from flask import render_template
from flask import request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def Job():
    db_sess = db_session.create_session()
    news = db_sess.query(Jobs)
    return render_template("base.html", jobs=news)


def main():
    db_session.global_init("db/blogs.db")
    user = User()
    user.surname = "Scott"
    user.name = "Ridley"
    user.age = 21
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Рей"
    user.name = "Ридл"
    user.age = 21
    user.position = "sequreti"
    user.speciality = "robots engineer"
    user.address = "module_2"
    user.email = "Рей_Ридл@mars.org"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Merser"
    user.name = "Alex"
    user.age = 21
    user.position = "arheolog"
    user.speciality = "engineer"
    user.address = "module_3"
    user.email = "Merser_Alex@mars.org"
    db_sess.add(user)
    db_sess.commit()

    user = User()
    user.surname = "Jk"
    user.name = "Htirlec"
    user.age = 21
    user.position = "pilot"
    user.speciality = "Pilot"
    user.address = "module_4"
    user.email = "Jk_Htirlec@mars.org"
    db_sess.add(user)
    db_sess.commit()
    app.run()
    
    news = Jobs(job="deployment of residential modules 1 and 2",
                collaborators="2, 3", is_finished=True,
                work_size=15, user=user)
    db_sess.add(news)
    db_sess.commit()
    
    job = db_sess.query(Jobs).filter(Jobs.id == 1).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=15)
    user = db_sess.query(User).filter(User.id == 2).first()
    news = Jobs(job="explorant of mineral resurse",
                collaborators="3, 4", is_finished=False,
                work_size=14, user=user)
    db_sess.add(news)
    db_sess.commit()
    
    job = db_sess.query(Jobs).filter(Jobs.id == 2).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=14)
    user = db_sess.query(User).filter(User.id == 3).first()
    news = Jobs(job="deployment of manager system",
                collaborators="2, 4", is_finished=False,
                work_size=48, user=user)
    db_sess.add(news)
    db_sess.commit()
    
    job = db_sess.query(Jobs).filter(Jobs.id == 3).first()
    job.finished_date = datetime.datetime.now() + datetime.timedelta(hours=48)
    db_sess = db_session.create_session()
    app.run()


if __name__ == '__main__':
    main()
