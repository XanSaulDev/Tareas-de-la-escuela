#   Huerta Murillo Alejandro Saul 
#   Jennyfher Jacquelinne Casillas Rendon
#   Alfonso Guadalupe Chanes Flores
#   Script que simula un cajero automático.
#   26/05/22

def ATM():
    bal=0
    op=0
    movs=[]
    while op != 5:
        #datos de salida
        print("""\nCajero
    1. Ver mi saldo
    2. Depositar
    3. Retirar
    4. Movimientos
    5. Salir
        """)
        #datos de salida y entrada
        op=int(input("Opción: "))
        #proceso
        if op in range(1,6):
            if op == 1:
                #datos de salida
                print(f"\n----------Tu saldo es: {bal}----------")
            elif op == 2:
                #datos de salida y entrada
                amount=float(input("\nCuanto deseas depositar: "))
                if amount > 0:
                    #proceso
                    bal += amount
                    #datos de salida
                    movs.append("Deposito $"+str(amount))
                else:
                    #datos de salida
                    print("\nNo puedes depositar una cantidad negativa")
            elif op == 3:
                #datos de salida y entrada
                amount=float(input("\nCuanto deseas retirar: "))
                if amount > bal or amount < 0:
                    #datos de salida
                    print("No hay suficiente saldo")
                else:
                    #proceso
                    bal -= amount
                    #datos de salida
                    print(f"----------Tu saldo es: {bal}------------")
                    movs.append("Retiro $"+str(amount))
            elif op == 4:
                #datos de salida
                print(*movs, end="\n")
            elif op == 5:
                #datos de salida
                print("\nHasta luego")
                exit()
            
        else:
            ATM()
ATM()