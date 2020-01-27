# -*- coding: utf-8 -*-
"""
Created on SAT Jan 25 2020

Leo el .xml que devuelve la aplicación de onos e inserto esos valores en una base de datos

@author: Cesareo
"""

import xml.etree.ElementTree as ET


#Inicio del programa
def main():    
	xml = ET.parse('/home/cesareo/GIT/statistics-collector-onos/pyDB/resultado.xml')   
	raiz = xml.getroot()
	roota = raiz.findall('./root/')      #Me voy a la rama de mis objetos xml
	elementos = []      #En esta lista guardaré (sin repetir) cada una de las hojas que tenga el excel

	for switch in roota:
		for puerto in switch:
			print(puerto.tag , puerto.text)


if __name__ == '__main__':
	main()     
