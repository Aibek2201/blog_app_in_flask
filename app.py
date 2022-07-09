from flask import Flask, render_template, flash, session, redirect, request
from flask_bootstrap import Bootstrap
from flask_mysqldb import MySQL
import yaml, os 

app = Flask(__name__)
Bootstrap(app)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['SECRET_KEY'] = os.urandom(24)
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/blogs/<int:id>')
def blogs(id): 
    return render_template('blogs.html', blog_id = id)


@app.route('/register/',methods = ['GET','POST'])
def register(): 
    if request.method == 'POST':
        user_details = request.form
        if user_details['password'] != user_details['confirmPassword']:
            flash('Passowrds do not match! Try again!', 'danger')
            return render_template('register.html')
        cursor = mysql.connection.cursor()
        
    return render_template('register.html')


@app.route('/login/',methods = ['GET','POST'])
def login(): 
    return render_template('login.html')


@app.route('/write-blog/',methods = ['GET','POST'])
def write_blog(): 
    return render_template('write-blog.html')


@app.route('/my-blogs/')
def my_blogs(): 
    return render_template('my-blogs.html')


@app.route('/edit-blog/<int:id>',methods = ['GET','POST'])
def edit_blog(id): 
    return render_template('edit-blog.html', blog_id = id)


@app.route('/delete-blog/<int:id>', methods = ['POST'])
def delete_blog(id): 
    return "Successfully deleted"


@app.route('/logout/')
def logout(): 
    return render_template('logout.html')






if __name__ == '__main__':
    app.run() 