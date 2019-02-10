# dc_project2

This application saves a users location based on longitude and latitude coordinates and the Google GeoLocation API.
A user can save a number of addresses along with a note to give more context to the address. The idea is that there may be a need for a quick way to save an address while on the go in order to use it to look something up related to the address at a later time. 

The live application can be found [here](https://capturewhere.herokuapp.com).

To run locally:

Prereqs:
--python 2.7+
--pipenv, `pip install pipenv`
--SECRET_KEY/GEO_API_KEY, create an .env file and set these two environment variables. You will need a google developer account 
  and get an api key for the GeoLocation API. See [here](http://flask.pocoo.org/docs/1.0/config/#SECRET_KEY) for the SECRET_KEY setup.


1. clone the repo and cd into main directory.
2. run pipenv install  (this was coded using python 2.7.15, but python 3+ should also be fine)
3. run pipenv shell
4. run python run.py
5. go to localhost:5000 to see app.
