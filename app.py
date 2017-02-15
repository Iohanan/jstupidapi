from flask.ext.api import FlaskAPI
from src import acompound_interest

app = FlaskAPI(__name__)

@app.route('/amount/<string:type>/<float:capital>/<float:interest>/<float:time_interest>')
def amount(capital, interest, time_interest):
	pass

@app.route('/interest/<string:type>/<float:capital>/<float:interest>/<float:time_interest>')
def capital(amount, interest, time_interest):
	pass

@app.route('/interest/<string:type>/<float:amount>/<float:capital>/<float:time_interest>')
def interest(amount, capital, time_interest):
	pass

@app.route('/timeinterest/<string:type>/<float:amount>/<float:capital>/<float:interest>')
def time_interest(amount, capital,interest):
	pass

if __name__ == '__main__':
	app.run()