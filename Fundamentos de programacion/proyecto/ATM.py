#ATM

def ATM():
    bal=0
    op=0
    movs=[]
    while op != 5:
        print("""\nCajero
    1. Ver mi saldo
    2. Depositar
    3. Retirar
    4. Movimientos
    5. Salir
        """)
        op=int(input("Opción: "))
        if op in range(1,6):
            if op == 1:
                print(f"\n----------Tu saldo es: {bal}----------")
            elif op == 2:
                amount=float(input("\nCuanto deseas depositar: "))
                if amount > 0:
                    bal += amount
                    movs.append("Deposito $"+str(amount))
                else:
                    print("\nNo puedes depositar una cantidad negativa")
            elif op == 3:
                amount=float(input("\nCuanto deseas retirar: "))
                if amount > bal or amount < 0:
                    print("No hay suficiente saldo")
                else:
                    bal -= amount
                    print(f"----------Tu saldo es: {bal}------------")
                    movs.append("Retiro $"+str(amount))
            elif op == 4:
                print(*movs, end="\n")
            elif op == 5:
                print("\nHasta luego")
                exit()
            
        else:
            ATM()
ATM()