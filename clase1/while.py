opcion=0
num1=int(input("ingrese numero 1"))
num2=int(input("ingrese numero 2"))
rpta=int
while True:
    print("""opciones:
    1)suma
    2)resta
    3)division
    4)potencia
    5)salir""")
    opcion=int(input("ingrese la operacion a realizar"))
    if opcion==1:
        print("la suma es: ", num1 + num2)
        print("desea realiza otra operaion? s/n")
        rpta=input()
        if rpta=="s":
            continue
        else:
            break
        
    elif opcion ==2:
        print("la resta es: ", num1 - num2)
        print("desea realiza otra operaion? s/n")
        rpta=input()
        if rpta=="s":
            continue
        else:
            break
    elif opcion == 5:
        print("bay")
        break
    elif opcion == 3:
        print("la divion es", num1/num2)
        print("desea realiza otra operacion s/n")
        rpta=input()
        if rpta=="s":
            continue
        else:
            break

    
    