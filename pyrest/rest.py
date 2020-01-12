from flask import Flask, jsonify, subprocess

app = Flask(__name__)

@app.route("/bytes" ,methods=["GET"])
def getBytes():
	ordenar()
	file = open ('/home/cesareo/Resultados/bytes/*.xml','r')
	bytes = file.read()
	return bytes 
	file.close()

@app.route("/bytes/2" ,methods=["GET"])
def getBytes():
	ordenar()
	file = open ('/home/cesareo/Resultados/bytes_2/*.xml','r')
	bytes = file.read()
	return bytes 
	file.close()


@app.route("/bytes/4" ,methods=["GET"])
def getBytes():
	ordenar()
	file = open ('/home/cesareo/Resultados/bytes_4/bytes.xml','r')
	bytes = file.read()
	return bytes 
	file.close()

@app.route("/packets" ,methods=["GET"])
def getPackets():
	ordenar()
	file = open ('/home/cesareo/Resultados/packets/packets.xml','r')
	packets = file.read()
	return packets 
	file.close()

def ordenar():
	subprocess.call(['./ordenar.sh'])
	

if __name__== '__main__':
	app.run(port=8080)
