# Desarrollo de un servicio de recolección de estadísticas para plataforma ONOS/SDN

### estadisticas

Aplicación ONOS desarrollada en java, que recolecta estadísticas de los switches desplegados en una red SDN. Compilar con maven:

```sh
$ mvn clean install
```

Instalar en el controlador:

```sh
$ onos-app localhost install target/*.oar
```

### pyDB

Aplicación desarrollada en Python, que constantemente lee el fichero .XML generado por la aplicación ONOS, estadísticas, para insertar esta información en la base de datos:

```sh
$ python insert.py
```

### pyREST

Aplicación desarrollada con el framework Flask, en Python, que levanta un servidor escuchando peticiones a los endpoints implementados:

```sh
$ python main.py
```

### resources

Colección Postman con todas las llamadas disponibles.
