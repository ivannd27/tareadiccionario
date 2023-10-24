nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")
direccion = input("Dime tu direccion: ")
telefono = input("Dime tu telefono: ")
datos = {"nombre" : nombre, "edad" : edad, "direccion" : direccion, "telefono" : telefono}
print(datos.get("nombre"), "tiene", datos.get("edad"), "vive en", datos.get("direccion"), "y su numero de telefono es ", datos.keys("telefono"))