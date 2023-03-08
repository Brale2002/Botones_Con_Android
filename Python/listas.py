listasCiudades = ["armenia","pereira","manizales","medellin","cali"]
# print(listasCiudades)
# list()
# print(list())
# creacion de listas
shopping = ["Agua","Huevos","Aceite","Sal","Limón"]
# imprimir datos del arreglo
print(shopping[0:3],shopping[2:4])
# se invierte la lista
print(shopping[::-1])
# si se utiliza shopping.reverse() no sirve print(list(reversed(shopping)))  pero los dos son para darle reversa a la lista
shopping.reverse()
print(shopping)
print(list(reversed(shopping)))
# se imprime la lista sin contenido
print(shopping[5:])
print(shopping[6:])
# inicia de atras para adelante y se devuelve todas las veces que le ordene(-5) y luego se devuelve hasta el numero que le ordene (4)
print(shopping[-5:4])
# para añadir al final de la lista
shopping.append("Atún")
print(shopping)

# se agregan elementos a la lista por medio de un siclo for poco a poco
even_numbers = []
for i in range(20):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers)

# para agregar datos a la lista con el metodo insert por medio de el indice
shopping.insert(1,"Jamón")
print(shopping)


# agregar datos a la lista
shopping.insert(100,"arroz")
print(shopping)
shopping.insert(-100,"arroz")
print(shopping)

# se agrega a lo ultimo de la lista
shopping.append(45)
print(shopping)


# se triplica los datos de la lista
print(shopping * 3)

# se le agregan los datos de la segunda lista a la primera 
shopping.extend(listasCiudades)
print(shopping)

# con extend se destructura la palabra que agregas a la lista
shopping.extend("Limón")
print(shopping)

# se le agregan los datos de la segunda lista a la primera pero en lista
shopping.append(listasCiudades)
print(shopping)


