from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


##########################################################
# HTML
##########################################################


@app.route('/')
def index():
    return render_template("hello.html")

##########################################################
# API
##########################################################


@app.route('/api/hello')
def api_hello():
    return '<h1>hello world</h1>'


# parameter
@app.route('/api/hello/<username>')
def api_string(username):

    if username == 'world':
        return redirect(url_for('api_hello'))  # redirect

    return {'Hello': username}


@app.route('/api/page/<int:pageId>')  # <float:no>
def api_int(pageId):
    return {'page is': pageId}

##########################################################
# etc
##########################################################


with app.test_request_context():
    # ('함수이름', params=value)
    print(url_for('api_string', username='hong'))


##########################################################
# run
##########################################################

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

# https://roksf0130.tistory.com/94?category=780144