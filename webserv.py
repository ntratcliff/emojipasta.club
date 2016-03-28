from flask import Flask
import emoji
app = Flask(__name__)

@app.route('/gen')
def generate():
	return emoji.generate()

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=22109)
