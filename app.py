from flask import Flask, render_template
app = Flask(__name__)

# BLUEPRINTS
from users.views import users_blueprint
from blog.views import blog_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(blog_blueprint)

@app.route('/')
def index():
    return render_template('index.html', name = "Chizuru")

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()