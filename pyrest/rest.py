from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/resultado" ,methods=["GET"])
def getBytes():
	file = open ('/home/cesareo/Resultados/resultado.xml','r')
	bytes = file.read()
	return bytes 
	file.close()

if __name__== '__main__':
	app.run(port=8080)
