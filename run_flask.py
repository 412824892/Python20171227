from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html',title='hi!')

@app.route('/services')
def services():
    return 'services'

@app.route('/about')
def about():
    return 'about'

if __name__ == '__main__':
    app.run(debug=True)
