from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/loginPage')
def login_page():
    return render_template('login.html')


@app.route('/success/<name>/<int:auth>')
def success_page(name, auth):
    info = {'name': 'hana', 'age': 25, 'phone': '01012345678'}
    return render_template('success.html', name=name, auth=auth, info=info)


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        form_name = request.form['name']
        return redirect(url_for('success_page', name=form_name, auth=200))

    else:
        query_name = request.args.get('name')
        return redirect(url_for('success_page', name=query_name, auth=500))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# https://roksf0130.tistory.com/94?category=780144