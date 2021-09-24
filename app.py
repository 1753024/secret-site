from flask import Flask, render_template, redirect, url_for, request, session
from functools import wraps
app = Flask(__name__)

app.secret_key = "S3cretAsFUCK"

@app.errorhandler(404)
def invalid_route(e):
	return render_template("404.html")



def login_required(f):
	@wraps(f)
	def wrap(*args,**kwargs):
		if('log_in' in session):
			return f(*args, **kwargs)
		else:
			return redirect(url_for('home'))
	return wrap

@app.route('/', methods=['GET','POST'])
def home():
	error = None
	if (request.method == 'POST'):
		if(request.form['username'] != 'admin' or request.form['password']!= 'admin123'):
			error='Invalid credential.'
		else:
			session['log_in'] = True
			return redirect(url_for('noice'))
	return render_template("index.html",error=error)

@app.route('/noice')
@login_required
def noice():
	return render_template('noice.html')

@app.route('/logout')
def logout():
	session.pop('log_in',None)
	return redirect(url_for('home'))

if __name__=='__main__':
	app.run(debug=False,port=3000)

