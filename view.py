from flask import Flask, render_template, request
import db
from bson import ObjectId

app = Flask(__name__)
def v(k, default=None):
	return request.values.get(k, default)

@app.route("/", methods=['POST', 'GET'])
def index():
	result = ''
	if request.method == 'POST':
		mongodb = 'mongodb://%s:%s/%s'%(v('server', "localhost"), v('port', "27017"), v('db'))
		db.mongo.connect(mongodb)
		query = 'db.mongo.%s.%s.find(%s)'% (v('db'), v('collection'), v('query'))
		result = eval(query)
	return render_template('index.html', result=result, server=v('server'),
                                         db=v('db'), collection=v('collection'),
                                         query=v('query'))

if __name__ == "__main__":
	app.run('0.0.0.0', debug=True)

