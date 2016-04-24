from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/hi", methods=['POST','GET'])
def mailin():
	subject = "no message"
	if request.method == 'POST':
		subject = request.form['subject']
		return subject
	return subject

if __name__ == "__main__":
	app.run()