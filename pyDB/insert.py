# -*- coding: utf-8 -*-
"""
Created on SAT Jan 25 2020

Leo el .xml que devuelve la aplicación de onos e inserto esos valores en una base de datos

@author: Cesareo

Entro en un switch y recorro todos sus valores, realmente solo me interesan switch.tag y datos.text, las etiquetas ya las conozco por posición
"""

import xml.etree.ElementTree as ET


#Inicio del programa
def main():    
	xml = ET.parse('resultado.xml')   
	raiz = xml.getroot()
	switchsID = []
	values = []

	for switch in raiz:
		for datos in switch:
			#print(switch.tag, datos.tag, datos.text)
			switchsID.append(switch.tag)
			values.append(datos.text)
	

	print (switchsID, values)


if __name__ == '__main__':
	main()     
