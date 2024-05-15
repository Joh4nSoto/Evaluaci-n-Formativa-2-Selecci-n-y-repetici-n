pika,otaku,pulpo,anguila = 0,0,0,0
valor_total = 0
descuento = 1
cupon = False
opc = None
def total ():
    salir = None
    while salir != 1:
        try:
            print("----------------------------")
            print(f"Carrito: ${valor_total}\n")
            print(f"Pikachu Rolls: {pika}")
            print(f"Otaku Roll: {otaku}")
            print(f"Pulpo Venenoso: {pulpo}")
            print(f"Anguila eléctrica: {anguila}")
            print("----------------------------")
            salir = int(input("Ingrese 1 para volver: "))
        except:
            print("Ingrese una opcion valida.")
while opc != 7:
    try:
        print('''   
            1. Pikachu Roll $4500
            2. Otaku Roll $5000
            3. Pulpo Venenoso Roll $5200
            4. Anguila Eléctrica Roll $4800
            
            5. Ver compras.
            6. Ingresar cupon
            7. Finalizar compra.
            ''')
        opc = int(input("Seleccione un producto: "))
        match opc:
            case 1:
                pika += 1
                valor_total += 4500
                print("Se ha agregado 1 Pikachu Roll al carrito.")
            case 2:
                otaku += 1
                valor_total += 5000
                print("Se ha agregado 1 Otaku Roll al carrito.")
            case 3:
                pulpo += 1
                valor_total += 5200
                print("Se ha agregado 1 Pulpo venenoso al carrito.")
            case 4:
                anguila += 1
                valor_total += 4800
                print("Se ha agregado 1 Anguila Eléctrica al carrito.")
            case 5:
                total()
            case 6:
                while True:
                    try:
                        print("Para salir escribe 1.")
                        cupon=str(input("Ingrese el Codigo del cupon: "))
                        if cupon == "soyotaku":
                            descuento -= 0.1
                            print("Se te aplico el descuento de un 10%")
                        elif cupon == "1":
                            break
                        else:
                            print("Este cupon no existe.")
                    except:
                        print("Error, vuelva a ingresar.")
    except:
        print("ingrese un numero valido.")
valor_final = valor_total * descuento
print(f'''
******************************
TOTAL PRODUCTOS: {pika+otaku+pulpo+anguila}
******************************
Pikachu Roll : {pika}
Otaku Roll : {otaku}
Pulpo Venenoso Roll: {pulpo}
Anguila Eléctrica Roll: {anguila}
******************************
Subtotal por pagar: ${valor_total}
Descuento por código: {100-(descuento*100)}%
TOTAL: ${valor_final}
''')