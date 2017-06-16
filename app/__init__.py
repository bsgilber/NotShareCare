from flask import Flask, render_template, json, request
from flask_googlemaps import GoogleMaps, Map, icons
from login.models import *
from dashboard.content_management import Content

app = Flask(__name__)
GoogleMaps(app)
app.config.from_object('config')

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route("/", methods=['GET','POST'])
def main():
	sndmap = Map(
		identifier="sndmap",
		lat=33.753746,
		lng=-84.386330,
        	zoom_control=False,
        	maptype_control=False,
        	scale_control=False,
        	streetview_control=False,
		markers=[
            	{
                'icon': icons.dots.blue,
                'lat':  33.759123,
                'lng':  -84.389980,
                'infobox': ("<h3>Camping Bag: $5/day</h3>"
			    "<img src='static/images/sleepingbag.jpg' style='width:60px;height:60px;'>"
			   )
            	},
            	{
                'icon': icons.dots.blue,
                'lat': 33.751759,
                'lng': -84.380210,
                'infobox': ("<h3>Canoe with Oars: $15/day</h3>"
                            "<img src='static/images/canoe.jpg' style='width:60px;height:60px;'>"
                           )
 	    	},
            	{
                'icon': icons.dots.blue,
                'lat': 33.752750,
                'lng': -84.387440,
                'infobox': ("<h3>4-Person Tent: $8/day</h3>"
                            "<img src='static/images/tent.jpg' style='width:60px;height:60px;'>"
                           )
		},
                {
                'icon': icons.dots.blue,
                'lat': 33.748321,
                'lng': -84.390001,
                'infobox': ("<h3>Rock Climbing Rope and Helmets: $12/day</h3>"
                            "<img src='static/images/rope.jpg' style='width:60px;height:60px;'>"
                           )
                },
                {
                'icon': icons.dots.blue,
                'lat': 33.741341,
                'lng': -84.368931,
                'infobox': ("<h3>Bicycle, No Helmet: $1/hr</h3>"
                            "<img src='static/images/bicycle.jpg' style='width:60px;height:60px;'>"
                           )
                }
		])
	return render_template('index.html', sndmap=sndmap)

@app.route("/dashboard/")
def dashboard():
	return render_template('dashboard.html', TOPIC_DICT=Content())

@app.route('/login', methods=['POST','GET'])
def signUp():
	try:
		# read the posted values from the UI
		_name = request.form['inputName']
		_email = request.form['inputEmail']
		_password = request.form['inputPassword']
 
		# validate the received values
		if _name and _email and _password:
			newUser = UserModel(_name, _password, _email)
			db.session.add(newUser)
			db.session.commit()
			return json.dumps({'html':'<span>All fields good !!</span>'})
		else:
			return json.dumps({'html':'<span>Enter the required fields</span>'})
		
	except Exception as e:
		return json.dumps({'error':str(e)})
