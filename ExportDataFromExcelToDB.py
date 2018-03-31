#! /usr/bin/python

import xlrd
import MySQLdb

#Abrir el archivo
libro_excel = xlrd.open_workbook("NOMBRE_DEL_ARCHIVO.xls")

#Puedes leer con el nombre de la pestana o con el index numerico
#hoja = libro_excel.sheet_by_name("Hoja1")

hoja = libro_excel.sheet_by_index(0)

#--------- Conexion a MySQL ---------
conexion = MySQLdb.connect(host="HOST", user="USUARIO", passwd="CONTRASENA", db="NOMBRE_DB")

#Cursor para convertir la informacion linea por linea
cursor = conexion.cursor()

#con %s se previene de inyecciones SQL
query = """INSERT INTO NOMBRE_TABLA (param1,param2,param3,param4,param5) VALUES(%s, %s, %s, %s, %s)""";

#Ciclo para interactuar con el archivo XLS iniciando en la fila 2 (para saltar las cabeceras)
for m in range(1,hoja.nrows):
	parametro_uno = hoja.cell(m,0).value
	parametro_dos = hoja.cell(m,1).value
	parametro_tres = hoja.cell(m,2).value
	parametro_cuatro = hoja.cell(m,3).value
	parametro_cinco = hoja.cell(m,4).value
	#Asiganacion de valores para cada registro
	valores = (parametro_uno,parametro_dos,parametro_tres,parametro_cuatro,parametro_cinco)
	#Ejecucion del Query
	cursor.execute(query, valores)
#Cerrar el cursor para dejar de convertir informacion
cursor.close()
#Confirmar la transaccion de datos
conexion.commit()
#Cerrar la conexion de la DB
conexion.close()
