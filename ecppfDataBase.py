import psycopg2
connection = psycopg2.connect(database="ECPPF",user="postgres",password="Svr135Astivik")
cursor = connection.cursor()

def traerProveedor (nit):
	sql="select * where nit="+nit+";"
	cursor.execute(sql)
	
	for texto in cursor.nit( ):
  		print texto

  	return cursor

connection.close()