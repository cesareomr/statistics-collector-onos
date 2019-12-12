from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bytes" ,methods=["GET"])
def getBytes():
	file = open ('/tmp/onos-1.14.0/apache-karaf-3.0.8/bytes.xml','r')
	bytes = file.read()
	return bytes 
	file.close()
	
@app.route("/packets" ,methods=["GET"])
def getPackets():
	file = open ('/tmp/onos-1.14.0/apache-karaf-3.0.8/packets.xml','r')
	packets = file.read()
	return packets 
	file.close()

if __name__== '__main__':
	app.run(port=8080)
