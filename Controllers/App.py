from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'Post_sale'
mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('User.html')

if __name__ == '__main__':
    app.run(port=3000, debug=True)