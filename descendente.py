def calculo():
   x = int(0)
   y = int(0)
   num1 = int(input("inserte un numero: "))
   num2 = int(input("inserte otro numero: "))

   f = open('descendente.txt','a')
   if num1 < num2:
     x = num2
     y = num1
   else:
     x = num1
     y = num2
   while x >= y:
       print(x)
       f.write('\n'+str(x))
       x = x - 1
   f.close()
calculo()
