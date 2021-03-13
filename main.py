# coding=utf-8
import Bd2
import Operaciones
import csv
import ecppfDataBase
import operator
# Leer el archivo 'datos.csv' con reader() y 
# mostrar todos los registros, uno a uno:
listaControl = []
listaEnvio = []
listaOperacion = []
textoEnvioControl = "<h3>Se envio notificacion de pagos por correo electronico a los siguientes proveedores</h3>"
textoEnvioControl += '<br></br><table BORDER bordercolor="black" CELLPADDING=10 CELLSPACING=0><tr><th>No</th><th>RAZON SOCIAL PROVEEDOR</th><th>CORREO ENVIO NOTIFICACION</th></tr>'
noEnviado=""
y=0

with open('ProyectosPersonales\ECPPF\docOrigen.csv') as csvarchivo:
    entrada = csv.reader(csvarchivo)
    
    textoEnvio = ""

    for reg in entrada:
        if reg[0] in listaControl:
            textoEnvio += "<tr><td ALIGN=right>" + reg[3] + "</td><td ALIGN=right>" + reg[8] + "</td><td ALIGN=right>" + reg[4] + "</td><td ALIGN=right>" + reg[5] + "</td><td ALIGN=right>" + reg[6] + "</td><td ALIGN=right>" + reg[7] + "</td></tr>"
        else:
            if textoEnvio:
                textoEnvio += "</table><br></br><br></br><p>Agradecemos distribuir esta informacion al personal de su empresa que le puedan ser util estos datos.</p>"
                textoEnvio += "<br></br><br></br><footer><strong>POR FAVOR NO RESPONDER A ESTA CUENTA DE CORREO, NADIE MONITOREA ESTOS MENSAJES Y SE ELIMINAN AUTOMATICAMENTE.</strong></footer>"
                listaEnvio.append(textoEnvio)
                textoEnvio = ""

            listaControl.append(reg[0])
            textoEnvio += "<h3>Cordial Saludo.</h3>"
            textoEnvio += "<br></br><h3>Industrias Astivik le informa, que se realizo una transferencia el dia " + reg[2] + " a su cuenta bancaria No " + reg[1] + "</h3>"
            textoEnvio += "<br></br><p>Las facturas pagadas fueron las siguientes:</p>"
            textoEnvio += '<br></br><table BORDER bordercolor="black" CELLPADDING=10 CELLSPACING=0><tr><th>No FACTURA</th><th>VALOR NETO FACTURA</th><th>VALOR RET ICA</th><th>VALOR RET IVA</th><th>VALOR RET RENTA</th><th>VALOR PAGADO</th></tr>'
            textoEnvio += "<tr><td>" + reg[3] + "</td><td ALIGN=right>" + reg[8] + "</td><td ALIGN=right>" + reg[4] + "</td><td ALIGN=right>" + reg[5] + "</td><td ALIGN=right>" + reg[6] + "</td><td ALIGN=right>" + reg[7] + "</td></tr>"

    textoEnvio += "</table><br></br><br></br></p>Agradecemos distribuir esta informacion al personal de su empresa que le puedan ser util estos datos.</p>"
    textoEnvio += "<br></br><br></br><footer><strong>POR FAVOR NO RESPONDER A ESTA CUENTA DE CORREO, NADIE MONITOREA ESTOS MENSAJES Y SE ELIMINAN AUTOMATICAMENTE.</strong></footer>"
    listaEnvio.append(textoEnvio)

print "TOTAL REGISTROS A PROCESAR %d " % (len(listaControl))

for i in range(len(listaControl)):
    listaOperacion = Bd2.main(listaControl[i])
    #print listaOperacion
    x=0
    
    for filas in listaOperacion:
        if not filas:
            noEnviado+= "<br></br>"+((listaControl[i]))
            print "NO SE PUDO ENVIAR CORREO A %s " % ((listaControl[i]))
        else:
            if filas[2]:
                y+=1
                try:
                    Operaciones.envioCorreo("info@astivik.com.co", (filas[x+2]), listaEnvio[i])
                    textoEnvioControl += "<tr><td ALIGN=center>" + str(y) + "</td><td ALIGN=left>" + (filas[x+1]) + "</td><td ALIGN=left>" + (filas[x+2]) + "</td></tr>"
                    print "SE ENVIO CORREO A %s -- %s al correo %s " % ((filas[x]), (filas[x+1]), (filas[x+2]))
                except (RuntimeError, TypeError, NameError, IndexError):
                    print "NO ----------- %s " % ((listaControl[i]))
            else:
                noEnviado+= "<br></br>"+(filas[x])+" -- "+(filas[x+1])
                print "PROVEEDOR NO TIENE GUARDADO NINGUN CORREO ELECTRONICO %s -- %s " % ((filas[x]), (filas[x+1]))
        x+=3

textoEnvioControl += "</table><br></br><br></br><p>A algunos proveedores no se les pudo enviar notificacion por que no tienen asignado actualmente una direccion de correo electronico en la base de datos de notificaciones.</p>"+noEnviado
Operaciones.envioCorreo("sistemas@astivik.com.co", "auxcontable@astivik.com.co", textoEnvioControl)
Operaciones.envioCorreo("sistemas@astivik.com.co", "contabilidad@astivik.com.co", textoEnvioControl)
Operaciones.envioCorreo("sistemas@astivik.com.co", "sistemas@astivik.com.co", textoEnvioControl)