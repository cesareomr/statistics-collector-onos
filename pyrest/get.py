from flask import Flask, jsonify

app = Flask(__name__)

#f = open ('/tmp/onos-1.14.0/apache-karaf-3.0.8/prueba_AAAA_MM_DD_HH_MM_SS.xml','r')
#accounts = f.read()
#accounts = [{'name':"Cesar", 'valor': 15}]

@app.route("/bytes" ,methods=["GET"])
def getAccounts():
	f = open ('/tmp/onos-1.14.0/apache-karaf-3.0.8/prueba_AAAA_MM_DD_HH_MM_SS.xml','r')
	bytes = f.read()
	return bytes 
	f.close()

if __name__== '__main__':
	app.run(port=8080)
