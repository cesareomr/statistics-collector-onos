from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bytes" ,methods=["GET"])
def getBytes():
	file = open ('/home/cesareo/Resultados/bytes.xml','r')
	bytes = file.read()
	return bytes 
	file.close()

@app.route("/packets" ,methods=["GET"])
def getPackets():
	file = open ('/home/cesareo/Resultados/packets.xml','r')
	packets = file.read()
	return packets 
	file.close()

if __name__== '__main__':
	app.run(port=8080)
