from flask import Flask, render_template, json, request, url_for
from flask_googlemaps import GoogleMaps, Map, icons
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object('config')

GoogleMaps(app)
mail=Mail(app)

@app.errorhandler(404)
def not_found(error):
	return render_template('404.html'), 404

@app.route("/response", methods=['POST','GET'])
def email_response():
	if request.method == 'POST':
		_name = request.form['name']
		_email = request.form['email']
		_message = request.form['message']

		send_email(_name,_email,_message)

	return render_template("email_confirm.html")


@app.route("/signup", methods=['POST','GET'])
def signUp():
	return render_template("signup.html")

@app.route("/learnmore", methods=['POST','GET'])
def learnMore():
	return render_template("learnmore.html")

@app.route("/launchdate", methods=['POST','GET'])
def launchDate():
	if request.method == 'POST':
		_username = request.form['username']
		_phone = request.form['phone']
		_email = request.form['email']

		send_email(_username, _email, _phone)

	return render_template("launchdate.html")

@app.route("/", methods=['POST','GET'])
def main():
	sndmap = Map(
		identifier="sndmap",
		lat=33.753746,
		lng=-84.386330,
        	zoom_control=False,
        	maptype_control=False,
        	scale_control=False,
		scroll_control=False,
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

def send_email(name, email, message):
	msg = mail.send_message(
		'You got email from an OAR user!',
		sender='bsgilber@gmail.com',
		recipients=['bsgilber@gmail.com'],
		body="The user " + name + " emailed you with the message \"" + message + ".\" You can get in touch with them at " + email + "."
		)
	return
