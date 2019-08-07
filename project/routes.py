import os
from flask import render_template, url_for, flash, redirect, jsonify, request
from project import app, db, bcrypt
from project.forms import SignupForm, LoginForm
from project.models import User, UserSchema, Address, AddressSchema
from flask_login import login_user, logout_user, current_user, login_required
import requests as req

@app.route('/')
def home():
    return redirect(url_for('signup'))
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if current_user.is_authenticated:
        return redirect(url_for('user_show'))
    if form.validate_on_submit():
        form = request.form
        hashed_pw = bcrypt.generate_password_hash(form['password']).decode('utf-8')
        user = User(email=form['email'], password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        flash('Account created for {}! You are now able to login.'.format(user.email), 'success')
        user_schema = UserSchema()
        user_result = user_schema.dump(user)
        return render_template('users/show.html', user=user)
    return render_template('users/new.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('user_show'))
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            flash("Welcome Back, {}!".format(user.email), 'success')
            return redirect(url_for('user_show'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
            render_template('/users/login.html', form=form)
    return render_template('users/login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/users/show', methods=['GET',])
def user_show():
    return render_template('users/show.html', user=current_user)

@app.route('/users/location', methods=['POST',])
def user_location():
    lat, long, note = [request.get_json()[k] for k in ['lat', 'long', 'note']]
    geo_api_key = os.environ.get('GEO_API_KEY')
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key={}".format(lat, long, geo_api_key)
    response = req.get(url)
    address = response.json()['results'][0]['formatted_address']
    address_obj = Address(location=address, note=note, user_id=current_user.id)
    db.session.add(address_obj)
    db.session.commit()
    addr_schema = AddressSchema()
    address_json = jsonify(addr_schema.dump(address_obj))
    if address_json:
        return address_json
    else:
        return jsonify({'error':'there was an error'})
    
@app.route('/address/delete/<int:id>', methods=['POST'])
def delete_address(id):
    address = Address.query.filter_by(id=id).first()
    if address:
        db.session.delete(address)
        db.session.commit()
    return redirect(url_for('user_show'))