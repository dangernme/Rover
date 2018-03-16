from flask import Flask, render_template ,request
import sys

app = Flask(__name__)  

@app.route('/') 
@app.route('/controls')
def controls():     
    return render_template("controls.html")

@app.route('/configuration') 
def configuration():     
	return render_template("configuration.html")
	
@app.route('/debug') 
def debug():     
	return render_template("debug.html")

if __name__ == "__main__":
    app.run()	