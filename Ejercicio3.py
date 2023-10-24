precios_frutas = { 'manzana': 0.80,'platano': 1.35,'pera': 0.85,'naranja': 0.70}
fruta = input("Ingresa el nombre de la fruta: ")
kilos = int(input("Ingresa la cantidad en kilos: "))
if fruta in precios_frutas:
    fruta_selec = precios_frutas[fruta]
    precio_total = fruta_selec * kilos
    print("El precio de es de:", precio_total, " €")
else:
    print("No está esta fruta") 