from flask import Flask
app = Flask(__name__)
@app.route('/')#home route
def index():
	return 'Hello World with Flask'
#app.run()
