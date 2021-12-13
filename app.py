from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')

@app.route("/auth/login")
def login():
	return render_template('login.html')

@app.route("/auth/callback")
def login_callback():
	return render_template('login_callback.html', data=request.args)

if __name__ == "__main__":
	app.run(port = 51023)
