
from flask import Blueprint, render_template, url_for,redirect
bp = Blueprint('admin', __name__, url_prefix='/admin')

@bp.route('/add')
def add():
    return "ADDED BOOK"

@bp.route('/login/<name>')
def login(name=None):
    if name and name == 'admin':
        return redirect(url_for('admin.home'))
    else:
        return redirect(url_for('admin.unauthorized'))


@bp.route('/unauthorized')
def unauthorized():
    return "NOT AUTHORIZED"

@bp.route('/home')
def home(name=None):
    return "HOME OF THE ADMINS"

@bp.route('/delete/')
@bp.route('/delete/<name>')
def delete(name="NOBOOK"):
    return f"DELETED BOOK {name}"

