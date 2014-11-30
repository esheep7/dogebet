from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/')
def index():
    return "Index Page"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
