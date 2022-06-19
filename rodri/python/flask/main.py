from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
import unittest

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRET'

todos = ["Comprar cafe", "Enviar solicitud de compra", "Entregar video a productor"]

class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Enviar")

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
    raise Exception(error)

@app.route('/')
def index():
    user_ip = request.remote_addr

    response = make_response(redirect("/hello"))
    # response.set_cookie("user_ip", user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip = request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    login_form = LoginForm()
    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito')

        return redirect(url_for('index'))

    # return f"Hello World Platzi, tu ip es {user_ip}"
    return render_template('hello.html', **context)