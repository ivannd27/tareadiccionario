diccionario = {'Euro':'€', 'Dollar':'$','Yen':'Y'}
divisa = input("Dime una divisa: ")

if divisa in diccionario:
    simbolo = diccionario[divisa]
    print(simbolo)
else:
    print("La divisa no está en el diccionario")