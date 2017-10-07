from flask import Flask, render_template, request
from columnar import columnarCipher
from caesar import caesarCipher
from vernam import oneTimePad
import operator

app = Flask(__name__)

@app.route('/')
def function():
	return render_template('index.html')

# Caesar Cipher
@app.route('/CaesarCipher')
def caesarIndex():
	return render_template('caesar.html')

@app.route('/caesarEncrypted', methods=['POST'])
def caesarEn():
	plainText = request.form['plain']
	key = request.form['key']
	return render_template('caesar.html', Encrpyt=caesarCipher(plainText, int(key)))

@app.route('/caesarDecrypted', methods=['POST'])
def caesaDe():
	plainText = request.form['encrypt']
	key = request.form['key']
	return render_template('caesar.html', Decrpyt=caesarCipher(plainText,-int(key)))
#===============================================================================

#Vernam One Time Pad
@app.route('/oneTimePadCipher')
def vernamIndex():
	return render_template('vernam.html')

@app.route('/vernamEncrypted', methods=['POST'])
def vernamEn():
	encrypted = oneTimePad(request.form['plain'], request.form['key'], operator.add)
	if encrypted == -1:
		return render_template('vernam.html', error="ERROR: sKey too short")
	else:
		return render_template('vernam.html', Encrpyt=encrypted)

@app.route('/vernamDecrypted', methods=['POST'])
def vernamDe():
	plainText = oneTimePad(request.form['encrypt'], request.form['key'], operator.sub)
	if plainText == -1:
		return render_template('vernam.html', error="ERROR: Key too short")
	else:
		return render_template('vernam.html', Decrpyt=plainText)
#===============================================================================

#Columnar Cipher
@app.route('/columnarCipher')
def columnarIndex():
	return render_template('columnar.html')

@app.route('/columnarEncrypted', methods=['POST'])
def columnarEn():
	encrypted = columnarCipher(request.form['plain'], request.form['key'])

	if encrypted == -1:
		return render_template('columnar.html', error="ERROR: Key too short")
	else:
		return render_template('columnar.html', Encrpyt=encrypted)

if __name__ == '__main__':
	app.run(debug=True)