from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template('index.html')


@app.route("/hi", methods=['GET','POST'])
def mailin():
    is_spam = request.form['X-Mailgun-SFlag'] == 'Yes'
    return request.form['subject']

if __name__ == "__main__":
    app.run()