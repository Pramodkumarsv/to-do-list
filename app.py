# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for simplicity
todos = []
todo_id_counter = 0

@app.route('/')
def index():
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    global todo_id_counter
    task = request.form.get('task')
    if task:
        todo_id_counter += 1
        todos.append({'id': todo_id_counter, 'task': task, 'completed': False})
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>')
def complete_todo(todo_id):
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = True
            break
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    global todos
    todos = [todo for todo in todos if todo['id'] != todo_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
