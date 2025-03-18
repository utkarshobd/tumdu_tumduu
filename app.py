from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        title = request.form.get('title')
        desc = request.form.get('desc')
        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()
        return redirect('/')

    alltodo = Todo.query.all()
    return render_template('index.html', alltodo=alltodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    
    if request.method == 'POST':
        todo.title = request.form['title']
        todo.desc = request.form['desc']
        db.session.commit()
        return redirect('/')

    return render_template('update.html', todo=todo)


@app.route('/delete/<int:sno>')
def delete(sno):  # Accepting sno as a parameter
    todo = Todo.query.filter_by(sno=sno).first()  # Fetch the todo item
    if todo:
        db.session.delete(todo)  # Delete the item
        db.session.commit()  # Save the changes
    return redirect('/')  # Redirect back to the home page
@app.route('/About')
# def about_page():
#     return render_template('utk.txt')
@app.route('/home')
def home_page():
    return render_template('index.html')    

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
