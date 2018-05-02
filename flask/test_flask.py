from flask import Flask, url_for

#基于flask的SPA项目 

app = Flask(__name__)
# 你可以用 url_for() 来给指定的函数构造 URL。它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。未知变量部分会添加到 URL 末尾作为查询参数
# @app.route('/')
# def hello_world():
#     return 'Hello World!'
@app.route('/')
def index():
    return 'Ferre Index Page'

@app.route('/hello')
def hello():
    return 'hello ferre'
@app.route('/user/<username>')

def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/about')
def reek():
    return 'The about page'

@app.route('/support')
def support():
    return 'The support page'

# with app.test_request_context():
#     print(url_for('login'))     #/login
    # print(url_for('profile', username='John Doe'))      #/user/John%20Doe

if __name__ == '__main__':
    app.run(debug=True)




