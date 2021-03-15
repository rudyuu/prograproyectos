def Menu():

    print( """************Calculadora************
_____________Menu____________ 
Segun el numero que presione se efectuara:
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir
______________________________""")
Menu()

def suma ():
   x = int(input("Ingrese Primer Numero\n"))
   y = int(input("Ingrese Segundo Numero\n"))
   print( "La Suma es:", x+y, "\n\n")
   Calculadora()

def resta():
   x = int(input("Ingrese Primer Numero\n"))
   y = int(input("Ingrese Segundo Numero\n"))
   print ("La Resta es:",x-y, "\n\n")
   Calculadora()

def mult():
   x = int(input("Ingrese Primer Numero\n"))
   y = int(input("Ingrese Segundo Numero\n"))
   print ("La Multiplicacion es:",x*y, "\n\n")
   Calculadora()

def div():
   x = int(input("Ingrese Primer Numero\n"))
   y = int(input("Ingrese Segundo Numero\n"))
   if (y==0):
      print ("No se Permite la Division Entre 0", "\n\n")
      Calculadora()
   else:
      print ("La Division es:", x/y, "\n\n")
      Calculadora()

def salir():
   print ("apagando calculadora")

def Calculadora():   
   try:
    opc = int(input("Selecione operacion\n"))
   except:
    print ("""\n\n
                  *_   _   _   _   _   _   _   _   _*
          ^       | `_' `-' `_' `-' `_' `_' `_' `_' |       ^
          |       |          Advertencia            |       |
          |       |Seleccione solo opciones del menu|       |
          |  (*)  |_   _   _   _   _   _   _   _   _|  \^/  |
          | _<">_ | `_' `-' `_' `-' `_' `_' `_' `_' | _(#)_ |
         o+o \ / \O                                 0/ \ / (=)
          0'\ ^ /\/                                 \/\ ^ /`0
            /_^_\ |                                 | /_^_\ 
            || || |                                 | || ||
            d|_|b_T_________________________________T_d|_|b
\n\n""")
    Menu()
    Calculadora()

   dict={
       1: suma,
       2: resta, 
       3: mult, 
       4: div,
       5: salir
   }
   try:
    dict.get(opc)()
   except:
    print ("""\n\n
                  *_   _   _   _   _   _   _   _   _*
          ^       | `_' `-' `_' `-' `_' `_' `_' `_' |       ^
          |       |          Advertencia            |       |
          |       |Seleccione solo opciones del menu|       |
          |  (*)  |_   _   _   _   _   _   _   _   _|  \^/  |
          | _<">_ | `_' `-' `_' `-' `_' `_' `_' `_' | _(#)_ |
         o+o \ / \O                                 0/ \ / (=)
          0'\ ^ /\/                                 \/\ ^ /`0
            /_^_\ |                                 | /_^_\ 
            || || |                                 | || ||
            d|_|b_T_________________________________T_d|_|b
\n\n""")
    Menu()
    Calculadora()                     
Calculadora()

