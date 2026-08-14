def guardar_datos():
    matriz = []
    lista_gastos = []
    matriz.append([]) # Presupuesto
    matriz.append(lista_gastos)
    matriz.append([]) # Total
    return matriz

def solicitar_datos(matriz):
    total = 0
    presupuesto = int(input("PRESUPUESTO: "))

    while presupuesto <= 0:
        print("PRESUPUESTO INVÁLIDO")
        presupuesto = int(input("PRESUPUESTO: "))

    matriz[0].append(presupuesto)
    finalizar = False

    while not finalizar:
        gastos = int(input("GASTOS: "))

        while gastos < 0 and gastos != -1:
            print("ERROR")
            gastos = int(input("GASTOS: "))

        if gastos == -1:
            finalizar = True
            matriz[2].append(total)
        else:
            total = total + gastos
            matriz[1].append(gastos)

def calcular_datos(matriz):
    print()
    print("==========================================================")
    print("======================= RESULTADOS =======================")

    if len(matriz[1]) != 0:

        c_multiplos = 0
        c_pares = 0
        acumulador = 0
        for i in range(len(matriz[1])):
            if matriz[1][i] % 100 == 0:
                c_multiplos = c_multiplos + 1
                print("MONTOS MULTIPLOS DE 100: ")
                print(matriz[1][i])
            if matriz[1][i] % 2 == 0:
                c_pares = c_pares + 1
                acumulador = acumulador + matriz[1][i]

        if matriz[0][0] < matriz[2][0]:
            print("LA EMPRESA HA SUPERADO EL PRESUPUESTO")
        elif matriz[0][0] > matriz[2][0]:
            print("LA EMPRESA NO HA SUPERADO EL PRESUPUESTO, GASTO BIEN.")
        else:
            print("LA EMPRESA ALCANZO EL PRESUPUESTO.")

        c_inferiores = 0 
        c_superiores = 0
        c_aux = 0
        if matriz[0][0] >= 15000:
            for j in range (len(matriz[1])):
                print(matriz[1][j])
                if matriz[1][j] < 15000:
                    c_inferiores = c_inferiores + 1
                elif matriz[1][j] > 15000:
                    c_superiores = c_superiores + 1
                else:
                    c_aux = c_aux + 1
        else:
            print()
            print("==========================================================")
            print("NO SE PUEDE IMPRIMIR EL CALCULO")
            print("EL PRESUPUESTO INGRESADO NO ALCANZO EL MONTO ESTABLECIDO.")
            print("==========================================================")
            print()
            return

        total = c_inferiores + c_superiores + c_aux
        porcentaje = (c_inferiores + c_aux) / total * 100

        print("CANTIDAD DE PARES:", c_pares, "MONTO ACUMULADO: ", acumulador)
        print(porcentaje,"%" " SON INFERIORES DE 15.000" , sep="")
        print("CANTIDAD MULTIPLOS DE 100: ", c_multiplos)
    
    else:
        print()
        print("NO SE INGRESARON GASTOS")
        print()

matriz = guardar_datos()
solicitar_datos(matriz)
calcular_datos(matriz)