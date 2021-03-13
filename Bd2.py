import psycopg2
import sys
import pprint

def main(nit):
    listaRs = []
    listaEnvio = []
  
    conn_string = "host='localhost' dbname='ECPPF' user='postgres' password='Svr135Astivik'"
    # print the connection string we will use to connect
    #print "Connecting to database\n	->%s" % (conn_string)
 
    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)
 
    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
 
    # execute our Query
    cursor.execute("SELECT * FROM proveedores where nit=%(id)s", {'id': nit})
 
    # retrieve the records from the database
    records = cursor.fetchall()
    #fila = list(records)
    #print fila[0]
    
    for fila in records:
    #for i in range(len(fila)):
        if  fila:
            listaRs.append(fila[1])
            listaRs.append(fila[2])
            listaRs.append(fila[3])
    
            #print "fila 1: %s fila2: %s Fila3: %s --- ListaRs: %s" % (fila[1], fila[2], fila[3], listaRs)
    
            listaEnvio.append(listaRs)
            #print listaEnvio
            #del listaRs[0:3]
            #print listaRs
            
            #print listaRs
	#print records[0][1]
	# print out the records using pretty print
	# note that the NAMES of the columns are not shown, instead just indexes.
	# for most people this isn't very useful so we'll show you how to return
	
	#print ""+records[0]+" - "+records[1]+" - "+records[2]+" - "+records[3]
	#pprint.pprint(records[0])
    
    return (listaEnvio)

if __name__ == "__main__":
	main(nit)