import os
from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/', methods=['GET'])
def index():
    """Render template Jinja."""
    return render_template('hello.html')

@site.route('/hello', methods=['GET'])
def hello():
    return '<h1>Hello from another page!</h1>'

@site.route('/cekdb', methods=['GET'])
def cekdb():
    is_database_working = True
    output = 'koneksi database ok'

    try:
        # to check database we will execute raw query
        db.session.query("1").from_statement("SELECT 1").all()
    except Exception as e:
        output = str(e)
        is_database_working = False

    return output

@site.errorhandler(404)
def error_404(error):
    """404 error handling."""
    return render_template('errors/404.html', error = error)
