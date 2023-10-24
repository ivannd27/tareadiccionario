meses = {'01': 'enero', '02' : 'febrero', '03' : 'marzo', '04' : 'abril', '05' : 'mayo', '06' : 'junio', '07' : 'julio', '08' : 'agosto', '09' : 'septiembre', '10' : 'octubre', '11' :'noviembre', '12' : 'diciembre'}
fecha = str(input("Dime una fecha en formato dd/mm/aaaa: "))
dia = fecha[0:2]
mes = fecha[3:5]
año = fecha[6:10]
if mes in meses:
    mes_selec = meses[mes]
    print(dia, "de", mes_selec, "del", año)
else:
    print("No existe esta fecha")
