def menu():
  print("\n____Ingrese un número entero, positivo y divisible entre 7 para calcular su factorial___\n")
menu()

def calculo():
  try:
   x = int(input("factorial de: "))
  except:
   print("ingrese un valor numerico")
   f = open('factorsiete.txt','a')
   f.write('\n' + 'el valor no era valido')
   f.close()
   menu()
   calculo()
  n = 0
  z = x
  div = x % 7 
 
  if div == 0:
    while (n + 1) < z:
        x = x * (n + 1)
        n = n + 1

    if x == 0:
        print("El resultado de 0! es 1")
        f = open('factorsiete.txt','a')
        f.write('\n' + 'El resultado de 0! es 1')
        f.close()
        calculo()
    elif x < 0:
        print("No existe factorial de negativos")
        f = open('factorsiete.txt','a')
        f.write('\n' + 'No existe factorial de negativos')
        f.close()
        calculo()
    else:
        print("El resultado de " + str(z) + "! es " + str(x))
        f = open('factorsiete.txt','a')
        f.write('\n' + "El resultado de " + str(z) + "! es " + str(x))
        f.close()
        calculo()
  else:
    print("no es divisible entre 7")
    calculo()
calculo()
