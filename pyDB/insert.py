# -*- coding: utf-8 -*-
"""
Created on SAT Jan 25 2020
@author: cesareomr

Swtich to english:

Leo el .xml que devuelve la aplicación de onos e inserto esos valores en una base de datos

Entro en un switch y recorro todos sus valores, realmente solo me interesan switch.tag y datos.text, las etiquetas ya las conozco por posición

Como mejora estaria bien que se parara solo cada x tiempo esperando
"""

import mysql.connector
import xml.etree.ElementTree as ET
import calendar
import time
from pathlib import Path
from os import remove

#Inicio del programa
def main():
	values = []
	mydb = mysql.connector.connect(host="localhost", user="root", passwd="root", database="bbddtfg")
	mycursor = mydb.cursor()
	my_file = Path("/home/cesareo/Resultados/resultado.xml")

	while True:
		if my_file.is_file():	# If resultado.xml exists
			time.sleep(3)
			xml = ET.parse("/home/cesareo/Resultados/resultado.xml")   # Don't work with $my_file
			raiz = xml.getroot()

			for switch in raiz:
				for datos in switch:
					values.append(datos.text)

				ts = calendar.timegm(time.gmtime())
				sql = "INSERT INTO STATISTICS (ROUTER, PORT, BYTESR, BYTESS, DURATION, PACKETSR, PACKETSRXD, PACKETSRXE, PACKETSS, PACKETSTXD, PACKETSTXE, TIMESTAMP) VALUES (%s, %s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s)"
				val = (switch.tag,values[0],values[1], values[2], values[3], values[4], values[5], values[6], values[7], values[8], values[9],ts)
				mycursor.execute(sql, val)
				mydb.commit()
				print("insert.py - OK | Inserccion realizada correctamente con marca de tiempo: " ,ts)
				del values[:]

			remove("/home/cesareo/Resultados/resultado.xml")

	

if __name__ == '__main__':
	main()     
