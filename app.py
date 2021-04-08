import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = 'task'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String)
    status = db.Column(db.Boolean)

    def __init__(self, description, status):
        self.description = description
        self.status = status


@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/insert', methods=['GET', 'POST'])
def insert():
    if request.method == 'POST':
        description = request.form.get('description')
        status = request.form.get('status')
        if status is None or status == 'False':
            status = False
        elif status == 'on' or status == 'True':
            status = True

        if description:
            task_exists = find_by_description(description)
            if task_exists:
                task_exists.status = status
            else:
                task = Task(description, status)
                db.session.add(task)
            db.session.commit()
        return redirect(url_for('find_all'))
    else:
        return render_template('insert.html')


@app.route('/find-all', methods=['GET'])
def find_all():
    tasks = Task.query.all()
    return render_template('list.html', tasks=tasks)


@app.route('/delete-by-id/<int:task_id>', methods=['GET', 'DELETE'])
def delete_by_id(task_id):
    task = find_by_id(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('find_all'))


@app.route('/change-status-by-id/<int:task_id>', methods=['GET', 'PUT'])
def change_status_by_id(task_id):
    task = find_by_id(task_id)
    if task.status:
        task.status = False
    else:
        task.status = True
    db.session.commit()

    return redirect(url_for('find_all'))


@app.route('/update-by-id/<int:task_id>', methods=['GET', 'POST', 'PUT'])
def update_by_id(task_id):
    task = find_by_id(task_id)
    description = request.form.get('description')

    if request.method == 'POST' or request.method == 'PUT':
        if description:
            task_exists = find_by_description(description)
            if task_exists:
                return render_template('update.html', task=task, message='Já existe um registro com essa descrição '
                                                                         'criado. Escolha outra descricão.')
            else:
                task.description = description
                db.session.commit()
        return redirect(url_for('find_all'))
    return render_template('update.html', task=task)


def find_by_id(task_id):
    db.session.remove()
    return Task.query.filter_by(_id=task_id).first()


def find_by_description(description):
    return Task.query.filter_by(description=description).first()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
