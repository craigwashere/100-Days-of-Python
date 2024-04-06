# to run: flask --app main --debug run
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import ValidationError, DataRequired

app = Flask(__name__)

#Optional: But it will silence the deprecation warning in the console.
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

class TaskForm(FlaskForm):
    task = StringField(label='Task', 
        validators=[
            DataRequired(message="This field is required.")
        ]
    )
    submit = SubmitField('Submit')

uncompleted_tasks = { }
       
# all Flask routes below
@app.route("/", methods=['GET', 'POST'])
def home():
    task_form = TaskForm()
        
    if request.method == 'POST':
        print(uncompleted_tasks)
        if task_form.validate_on_submit():
            if task_form.task.data in uncompleted_tasks.values():
                flash("To-Do already in list.")
            else:
                uncompleted_tasks[len(uncompleted_tasks)+1] = task_form.task.data
            
    return render_template("index.html", form = task_form, tasks = uncompleted_tasks)

@app.route('/delete/<id>')    
def delete(id):
    global uncompleted_tasks
    del uncompleted_tasks[int(id)]

    new_task_list = { }
    i = 1
    for key, value in uncompleted_tasks.items():
        print(value)
        new_task_list[i] = value
        i += 1
        
    uncompleted_tasks = new_task_list.copy()
    return redirect(url_for('home'))

print("__name__", __name__)

if __name__ == '__main__':
    print("main")
    app.run(debug=True)
