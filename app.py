from flask import Flask, render_template, request, url_for, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.create_all()


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
        if status is None:
            status = False
        else:
            status = True

        if description:
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
    task = Task.query.filter_by(_id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('find_all'))


@app.route('/change-status-by-id/<int:task_id>', methods=['GET'])
def change_status_by_id(task_id):
    task = Task.query.filter_by(_id=task_id).first()
    if task.status:
        task.status = False
    else:
        task.status = True
    db.session.commit()

    return redirect(url_for('find_all'))


@app.route('/update-by-id/<int:task_id>', methods=['GET', 'POST'])
def update_by_id(task_id):
    task = Task.query.filter_by(_id=task_id).first()
    description = request.form.get('description')

    if request.method == 'POST':
        if description:
            task.description = description
            db.session.commit()
            return redirect(url_for('find_all'))
    return render_template('update.html', task=task)


if __name__ == '__main__':
    app.run()
