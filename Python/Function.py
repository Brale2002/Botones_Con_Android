




cedula = 1091202432
clave = 123

saldoActual = 5000
cajero = True

def cajero(cedulaI,claveI,op,dinero):
  print("Bienvenido al cajero")
  if cajero == False:
    print ("cajero apagado")
  elif cedulaI == cedula and claveI == clave:
    print ("Los datos son correctos")
  elif op == "retirar":
    if dinero > saldoActual:
      print ("esta acción no se puede realizar")
    elif dinero < 0:
      print ("esta acción no se puede realizar")
    elif dinero - saldoActual :
      print ("Ha retirado dinero")

cajero(100000,123,"retirar",3000)