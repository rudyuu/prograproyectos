def Menu():

    print( """************Calculadora************
_____________Menu____________ 
Segun el numero que presione se efectuara:
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")
def Calculadora():

    Menu()
    opc = int(input("Selecione operacion\n"))
    while (opc >0 and opc <5):
        x = int(input("Ingrese Primer Numero\n"))
        y = int(input("Ingrese Segundo Numero\n"))
        if (opc==1):
            print( "La Suma es:", x+y)
            opc = int(input("\n****Selecione nueva operacion****\n"))
        elif(opc==2):
            print ("La Resta es:",x-y)
            opc = int(input("\n****Selecione nueva operacion****\n"))
        elif(opc==3):
            print ("La Multiplicacion es:",x*y)
            opc = int(input("\n****Selecione nueva operacion****\n"))
        elif(opc==4):
            try:
              print ("La Division es:", x/y)
              opc = int(input("\n****Selecione nueva operacion****\n"))
            except ZeroDivisionError:
              print ("No se Permite la Division Entre 0")
              opc = int(input("\n****Selecione nueva operacion****\n"))
Calculadora()
