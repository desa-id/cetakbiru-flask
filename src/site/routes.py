from flask import Blueprint, render_template

site = Blueprint('site', __name__)

@site.route('/')
def index():
    """Render template Jinja."""
    return render_template('hello.html')

@site.route('/hello')
def hello():
    return '<h1>Hello from another page!</h1>'

@site.errorhandler(404)
def error_404(error):
    """404 error handling."""
    return render_template('404.html', error = error)
