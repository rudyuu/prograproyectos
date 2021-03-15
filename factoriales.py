def menu():
  print("\n____Ingrese un número entero y positivo para calcular su factorial___\n")
menu()

def calculo():
  try:
   x = int(input("factorial de: "))
  except:
   print("ingrese un valor numerico")
   f = open('resultados factorial.txt','a')
   f.write('\n' + 'el valor no era valido')
   f.close()
   menu()
   calculo()
  n = 0
  z = x

  while (n + 1) < z:
      x = x * (n + 1)
      n = n + 1

  if x == 0:
      print("El resultado de 0! es 1")
      f = open('resultados factorial.txt','a')
      f.write('\n' + 'El resultado de 0! es 1')
      f.close()
      calculo()
  elif x < 0:
      print("No existe factorial de negativos")
      f = open('resultados factorial.txt','a')
      f.write('\n' + 'No existe factorial de negativos')
      f.close()
      calculo()
  else:
      print("El resultado de " + str(z) + "! es " + str(x))
      f = open('resultados factorial.txt','a')
      f.write('\n' + "El resultado de " + str(z) + "! es " + str(x))
      f.close()
      calculo()

calculo()
