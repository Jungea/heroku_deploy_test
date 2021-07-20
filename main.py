from flask import Flask, render_template, url_for, redirect, request

app = Flask(__name__)


@app.route('/loginPage')
def login_page():
    return render_template('login.html')


@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name


@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        form_name = request.form['name']
        return redirect(url_for('success', name=form_name))

    else:
        query_name = request.args.get('name')
        return redirect(url_for('success', name=query_name))


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# https://roksf0130.tistory.com/94?category=780144