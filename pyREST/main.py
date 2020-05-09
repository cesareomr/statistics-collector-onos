# coding=utf-8

# Revisar import necesarios
import pymysql, json, decimal, datetime, calendar, time
from app import app
from config import mysql
from decimal import Decimal
from flask import flash, request, jsonify

# Global variables
PORT = [1,2,3]
PORTS = ["1","2","3"]
ROUTERS = ["of_0000000000000001","of_0000000000000002","of_0000000000000003"]
ACTUAL = 1584887039
MAXTIME = 2280

def valor(resultado):
	primer=str(resultado).split(": ")
	segundo =str(primer[1]).split("}")
	return (int(segundo[0]))


# TOTAL DE CADA UNO

@app.route('/bytes/<string:sense>', methods=['GET'])
def bytes(sense):
	print("INFO - Entro en el metodo bytes")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))

	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)

		if sense == "received":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		elif sense == "sent":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		else:
			return notFound()

		resultado = {"Bytes " +sense: total}
		response = jsonify(resultado)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/packets/<string:sense>', methods=['GET'])
def packetsSimple(sense):
	print("INFO - Entro en el método packetsSimple")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))
	
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)

		if sense == "received":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		elif sense == "transmitted":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		else:
			return notFound()

		resultado = {"Packets " +sense: total}
		response = jsonify(resultado)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

@app.route('/packets/<string:sense>/<string:case>', methods=['GET'])
def packetsCompound(sense,case):
	print("INFO - Entro en el método packetsCompound")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))
		
	try:
		conn = mysql.connect()
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		if sense == "received" and case== "dropped":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		elif sense == "received" and case =="error":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		elif sense == "transmitted" and case == "dropped":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		elif sense == "transmitted" and case == "error":
			for x in ROUTERS:
				for y in PORT:
					while (x != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(x,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
		else:
			return notFound()
			
		resultado = {"Packets " +sense +" " +case: total}
		response = jsonify(resultado)
		response.status_code = 200
		return response
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()
		

# TODA LA INFO DE UN ROUTER

@app.route('/<string:id>')
def router(id):
	print("INFO - Entro en el método router")
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))
		
	if id in ROUTERS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			
			if tiempo == -1:
				cursor.execute("SELECT * FROM STATISTICS WHERE ROUTER=%s", id)
			elif tiempo <= MAXTIME and tiempo > 0:
				ts = calendar.timegm(time.gmtime(tiempo))
				nuevo = ACTUAL - ts
				cursor.execute("SELECT * FROM STATISTICS WHERE ROUTER=%s AND TIMESTAMP<%s",(id,nuevo))
			else:
				return badRequest()
				
			outQuery = cursor.fetchall()
			response = jsonify(outQuery)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()
		
	
# TOTAL DE CADA UNO EN UN ROUTER

@app.route('/<string:router>/bytes/<string:sense>', methods=['GET'])
def bytesRouter(router, sense):
	print("INFO - Entro en el método bytesRouter")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))

	if router in ROUTERS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)

			if sense == "received":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			elif sense == "sent":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			else:
				return notFound()

			resultado = {router +" bytes " +sense: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()

@app.route('/<string:router>/packets/<string:sense>', methods=['GET'])
def packetsRouterSimple(router, sense):
	print("INFO - Entro en el método packetsRouterSimple")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))

	if router in ROUTERS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)

			if sense == "received":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			elif sense == "transmitted":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			else:
				return notFound()

			resultado = {router +" packets " +sense: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()

@app.route('/<string:router>/packets/<string:sense>/<string:case>', methods=['GET'])
def packetsRouterCompound(router, sense, case):
	print("INFO - Entro en el método packetsRouterCompound")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))
	
	if router in ROUTERS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			if sense == "received" and case== "dropped":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			elif sense == "received" and case =="error":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			elif sense == "transmitted" and case == "dropped":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			elif sense == "transmitted" and case == "error":
				for y in PORT:
					while (router != ROUTERS[0] or y != PORT[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,y))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,y,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
							break
						else:
							return badRequest()
			else:
				return notFound()
			
			resultado = {router +" packets " +sense +" " +case: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()


# TOTAL DE CADA UNO EN CADA PUERTO DE CADA ROUTER

@app.route('/<string:router>/<string:port>/bytes/<string:sense>', methods=['GET'])	#PORT trantandolo como int, peta el execute
def bytesRouterPort(router, port, sense):
	print("INFO - Entro en el método bytesRouterPort")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))

	if router in ROUTERS and port in PORTS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)

			if sense == "received":
				if (router != ROUTERS[0] or port != PORTS[2]):
					if tiempo == -1:
						cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
						for row in cursor:
							outQuery = row
						total += valor(outQuery)
					elif tiempo <= MAXTIME and tiempo > 0:
						ts = calendar.timegm(time.gmtime(tiempo))
						nuevo = ACTUAL - ts
						cursor.execute("SELECT BYTESR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
						for row in cursor:
							outQuery = row
						total += valor(outQuery)
					else:
						return badRequest()
				else:
					return badRequest()
			elif sense == "sent":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT BYTESS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			else:
				return notFound()

			resultado = {router +" port:" +port +" bytes " +sense: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()


@app.route('/<string:router>/<string:port>/packets/<string:sense>', methods=['GET'])
def packetsRouterPortSimple(router, port, sense):
	print("INFO - Entro en el método packetsRouterPortSimple")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))

	if router in ROUTERS and port in PORTS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)

			if sense == "received":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSR FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			elif sense == "transmitted":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSS FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			else:
				return notFound()

			resultado = {router +" port:" +port +" packets " +sense: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()


@app.route('/<string:router>/<string:port>/packets/<string:sense>/<string:case>', methods=['GET'])
def packetsRouterPortCompound(router, port, sense, case):
	print("INFO - Entro en el método packetsRouterPortCompound")
	total = 0
	
	if request.args.get('time') == None:
		tiempo = -1
	else:
		tiempo = int(request.args.get('time'))
	
	if router in ROUTERS and port in PORTS:
		try:
			conn = mysql.connect()
			cursor = conn.cursor(pymysql.cursors.DictCursor)
			if sense == "received" and case== "dropped":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			elif sense == "received" and case =="error":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSRXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			elif sense == "transmitted" and case == "dropped":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXD FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			elif sense == "transmitted" and case == "error":
					if (router != ROUTERS[0] or port != PORTS[2]):
						if tiempo == -1:
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(router,port))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						elif tiempo <= MAXTIME and tiempo > 0:
							ts = calendar.timegm(time.gmtime(tiempo))
							nuevo = ACTUAL - ts
							cursor.execute("SELECT PACKETSTXE FROM STATISTICS WHERE ROUTER=%s AND PORT=%s AND TIMESTAMP<%s",(router,port,nuevo))
							for row in cursor:
								outQuery = row
							total += valor(outQuery)
						else:
							return badRequest()
					else:
						return badRequest()
			else:
				return notFound()
			
			resultado = {router +" port:" +port +" packets " +sense +" " +case: total}
			response = jsonify(resultado)
			response.status_code = 200
			return response
		except Exception as e:
			print(e)
		finally:
			cursor.close()
			conn.close()
	else:
		return notFound()
		

# TIEMPO QUE LLEVA VIVO UN PUERTO

@app.route('/<string:id>/<string:case>/up', methods=['GET'])
def routerPortUp(id, case):
	print("INFO - Entro en el método routerPortUp")
	
	if id in ROUTERS:
		if case in PORTS:
			try:
				conn = mysql.connect()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				if (id != ROUTERS[0] or case != PORTS[2]):
					cursor.execute("SELECT DURATION FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(id,case))
					for row in cursor:
						outQuery = row
					response = jsonify(outQuery)
					response.status_code = 200
					return response
				else:
					return badRequest()
			except Exception as e:
				print(e)
			finally:
				cursor.close()
				conn.close()
		elif case=="max" or case=="min":
			try:
				conn = mysql.connect()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				total = []
				
				for y in PORT:
					while (id != ROUTERS[0] or y != PORT[2]):
						cursor.execute("SELECT DURATION FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(id,y))
						for row in cursor:
							outQuery = row
						total.append(valor(outQuery))
						break
				
				if case=="max":
					tiempo = max(total)
				else:
					tiempo = min(total)
				pos = (total.index(tiempo))+1
				resultado = {"Port:" +str(pos) +" Duration: ": str(tiempo)}
				response = jsonify(resultado)
				response.status_code = 200
				return response
			except Exception as e:
				print(e)
			finally:
				del total [:]
				cursor.close()
				conn.close()
		else:
			return badRequest()
	elif id=="port":
		if case=="max" or case=="min":
			try:
				conn = mysql.connect()
				cursor = conn.cursor(pymysql.cursors.DictCursor)
				total = []
				
				for x in ROUTERS:
					for y in PORT:
						while (x != ROUTERS[0] or y != PORT[2]):
							cursor.execute("SELECT DURATION FROM STATISTICS WHERE ROUTER=%s AND PORT=%s",(x,y))
							for row in cursor:
								outQuery = row
							total.append(valor(outQuery))
							break
				if case=="max":
					tiempo = max(total)
				else:
					tiempo = min(total)
					
				pos = total.index(tiempo)
				if pos <= 1:
					rout = ROUTERS[0]
					puer = pos+1
				elif pos >=5:
					rout = ROUTERS[2]
					puer = pos-4
				else:
					rout = ROUTERS[1]
					puer = pos-1

				resultado = {"Router: " +rout +" port:" +str(puer) +" Duration: ": str(tiempo)}
				response = jsonify(resultado)
				response.status_code = 200
				return response
			except Exception as e:
				print(e)
			finally:
				del total [:]
				cursor.close()
				conn.close()
		else:
			return badRequest()
	else:
		return notFound()


@app.errorhandler(400)
def badRequest(error = None):
    message = {
        'status': 400,
        'message': 'Bad request: ' + request.url,	# Averiguar que variables puedo usar como esta, por ejemplo para los argumentos de tiempo
    }
    response = jsonify(message)
    response.status_code = 400
    return response

@app.errorhandler(404)
def notFound(error = None ):
    message = {
        'status': 404,
        'message': 'Resource not found: ' + request.url,
    }
    response = jsonify(message)
    response.status_code = 404
    return response

@app.errorhandler(500)
def internalServerError(error = None):
	message={
		'status':500,
		'message': 'Internal server Error'
	}
	response = jsonify(message)
	response.status_code = 500
	return response

		
if __name__ == "__main__":
    app.run()
    
