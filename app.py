import uuid
from flask import Flask, render_template, request, url_for, session, redirect
from functools import wraps
from streamlabs_interfacer import get_access_token, get_socket_token
import constants

app = Flask(__name__)
app.secret_key = constants.SESSION_SIGNING_KEY


def login_required(function):
	@wraps(function)
	def decorated(*args, **kwargs):
		print("hmmm" + session.get('streamlabs.code'))
		if session.get('streamlabs.code'):
			return function()  # TODO: Figure out how to forward args, I get an error for now

		return redirect(url_for('login'))

	return decorated


@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/auth/login")
def login():
	session['id'] = uuid.uuid4()
	return render_template('login.html')


@app.route("/auth/callback")
def login_callback():
	session['streamlabs.code'] = request.args.get('code')
	return redirect(url_for('dashboard'))


@app.route('/dashboard')
@login_required
def dashboard():
	access_token = get_access_token(session['streamlabs.code'])
	socket_token = get_socket_token(access_token)

	return render_template('login_callback.html')


@app.route("/api/open_socket")
def open_socket():
	# open the socket here
	return render_template('index.html')


if __name__ == "__main__":
	app.run(port = 51023)
