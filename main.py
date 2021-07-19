from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("hello.html")


@app.route('/api/')
def api_index():
    return {'Hello': 'World!'}


@app.route('/api/hello')
def api_hello():
    return '<h1>hello world</h1>'


if __name__ == "__main__":
    app.run(debug=True)
