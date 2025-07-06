from flask import Flask

app=Flask(__name__)

@app.route("/info")
def myinfo():
	return "i am Lakshya Chalana"


@app.route("/phone")
def myphone():
	return "888888"

app.run(host="0.0.0.0")