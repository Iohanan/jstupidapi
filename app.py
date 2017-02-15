from flask.ext.api import FlaskAPI
from src import acompound_interest
app = FlaskAPI(__name__)

@app.route('/test')
def test():
	return {'teste': 'teste '}

@app.errorhandler(404)
def teste():
	return 'ola'

if __name__ == '__main__':
	app.run()