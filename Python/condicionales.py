# a = 6
# if a >5:
#   if (a == 5):
#     print (f"{a} es mayor a 5")
# else : 
#   print (f"{a} es menor a 5")


# a = 5
# if a > 5:
#     print (f"{a} es mayor a 5")
# elif a == 4: 
#   print (f"{a} es menor a 5 y es mayor a 2")
# else: 
#   print ("----------------------------------------------------------------")


color = "rojo"
prendido = False
msj = "Semaforo prendido"

if prendido == False:
  print("semaforo apagado")
elif color == "verde":
  print (msj+", Puede seguir")
elif color == "amarillo":
  print(msj+", prepararse")
elif color == "rojo":
  print (msj+", parar")
elif color == "intermitente" :
  print ("Semaforo no funciona")
else :
  print("Semaforo dañado")


