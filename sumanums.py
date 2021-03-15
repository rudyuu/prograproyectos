def menu():
  print("\n____Ingrese un número entero y positivo\n")
menu()

def calculo():
  x = int(input("sumar hasta "))
  n = 0
  z = x

  while (n + 1) < z:
      x = x + (n + 1)
      n = n + 1
  print("el resultado de la suma es: ", x)
  f = open('sumanums.txt','a')
  f.write("\nel resultado de la suma es: "+ str(x))
  f.close()

calculo()
