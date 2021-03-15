import psycopg2

def Menu():

    print( """************************
               ingrese 3 numeros
              ************************""")
Menu()

def Calculadora():   
   try:
    num1 = int(input("primer numero\n"))
    num2 = int(input("segundo numero\n"))
    num3 = int(input("tercer numero\n"))
   except:
    print ("""\n\n
                  *_   _   _   _   _   _   _   _   _*
          ^       | `_' `-' `_' `-' `_' `_' `_' `_' |       ^
          |       |          Advertencia            |       |
          |       |     Solo son validos numeros    |       |
          |  (*)  |_   _   _   _   _   _   _   _   _|  \^/  |
          | _<">_ | `_' `-' `_' `-' `_' `_' `_' `_' | _(#)_ |
         o+o \ / \O                                 0/ \ / (=)
          0'\ ^ /\/                                 \/\ ^ /`0
            /_^_\ |                                 | /_^_\ 
            || || |                                 | || ||
            d|_|b_T_________________________________T_d|_|b
          \n\n""")
   conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
   cursor1=conexion.cursor()
   sql="insert into nums(n1,n2,n3,resultado) values (%s,%s,%s,%s)"
   if (num1==num2 and num1 != num3):
     print("el distinto es", num3)
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "el distinto es" + str(num3))
     f.close()
     datos=(num1,num2,num3,str(num3))
     cursor1.execute(sql, datos)

   elif (num1==num3 and num1 != num2):
     print("el distinto es", num2)
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "el distinto es" + str(num2))
     f.close()
     datos=(num1,num2,num3,str(num2))
     cursor1.execute(sql, datos)

   elif (num3==num2 and num1 != num3):
     print("el distinto es", num1)
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "el distinto es" + str(num1))
     f.close()
     datos=(num1,num2,num3,str(num1))
     cursor1.execute(sql, datos)

   elif (num1 > num2 and num1 > num3):
     print("la suma es", num1+num2+num3)
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "la suma es"+ str(num1+num2+num3))
     f.close()
     datos=(num1,num2,num3,str(num1+num2+num3))
     cursor1.execute(sql, datos)

   elif (num2 > num1 and num2 > num3):
     print("El producto es", num1*num2*num3)
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "el producto es"+ str(num1*num2*num3))
     f.close()
     datos=(num1,num2,num3,str(num1*num2*num3))
     cursor1.execute(sql, datos)

   elif (num3 > num2 and num3 > num1):
     print("concatenado: " + str(num1)+str(num2)+str(num3))
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "concatenado: " + str(num1)+str(num2)+str(num3))
     f.close()
     datos=(num1,num2,num3,str(num1)+str(num2)+str(num3))
     cursor1.execute(sql, datos)

   elif (num1==num2==num3):
     print("todos son iguales")
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "todos son iguales")
     f.close()
     datos=(num1,num2,num3,"todos son iguales")
     cursor1.execute(sql, datos)

   else:
     print("no esta en las opciones")
     f = open('3numeros.txt','a')
     f.write('\n'+ str(num1)+str(num2)+str(num3) + "no era opcion")
     f.close()
   conexion.commit()
   conexion.close()  
Calculadora()
