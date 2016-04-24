from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/hi", methods=['POST','GET'])
def mailin():
	subject = '<none>'
	if request.method == 'POST':
    	is_spam = request.form['X-Mailgun-SFlag'] == 'Yes'
    	subject = request.form['subject']
    return subject

if __name__ == "__main__":
    app.run()