from flask import Flask
app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'hello ferre'

if __name__ == '__main__':
    app.run(debug=True)




