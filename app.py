from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__, template_folder='templates')

todos = []

@app.route('/')
def hello():
    return render_template('index.html', todos=todos)

@app.route('/add-task', methods=["POST"])
def add():
    todo = request.form['todo']
    todos.append({'task': todo, 'done': False})
    return redirect(url_for('hello'))

@app.route('/edit-task/<int:index>', methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == 'POST':
        todo['task'] = request.form['todo']
        return redirect(url_for('hello'))
    else:
        return render_template('edit.html', todo=todo, index=index)

@app.route('/check/<int:index>')
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('hello'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[index]
    return redirect(url_for('hello'))

if __name__ == '__main__':
    app.run(debug=True)
