import time
import os

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bytes" ,methods=["GET"])
def getBytes():
	file = open ('/tmp/bytes.xml','r')
	bytes = file.read()
	return bytes 
	file.close()
	
@app.route("/packets" ,methods=["GET"])
def getPackets():
	file = open ('/tmp/packets.xml','r')
	packets = file.read()
	return packets 
	file.close()	
	
def main():
	print("¿Con qué frecuencia desea recoletar ( en segundos)?")
	tiempo = input()
	app.run(port=8080)
	
	while True:
		os.system('cp /tmp/onos-1.14.0/apache-karaf-3.0.8/bytes.xml /tmp/')
		os.system('cp /tmp/onos-1.14.0/apache-karaf-3.0.8/packets.xml /tmp/')
		time.sleep(tiempo) 
	
#Estaria bin captura la señal Ctrl^C para borrar /tmp/, no se si en algun caso cogerá mal el xml

if __name__== '__main__':
	main()
