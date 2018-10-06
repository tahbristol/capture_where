from flask import render_template, url_for, flash, redirect, jsonify, request
from project import app, db, bcrypt
from project.forms import SignupForm
from project.models import User, UserSchema
from flask_login import login_user, logout_user, current_user, login_required

@app.route('/')
def home():
	form = SignupForm()
	return render_template('index.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	form = SignupForm()
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	if form.validate_on_submit():
		form = request.form
		hashed_pw = bcrypt.generate_password_hash(form['password']).decode('utf-8')
		user = User(email=form['email'], password=hashed_pw)
		db.session.add(user)
		db.session.commit()
		flash('Account created for {}! You are now able to login.'.format(user.email), 'success')
		user_schema = UserSchema()
		user_result = user_schema.dump(user)
		return render_template('index.html', form=SignupForm())
	return render_template('index.html', form=form)