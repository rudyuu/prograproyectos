def Menu():

    print( """************Factorial de un numero************
_____________Menu____________ 
 despues de ingresar el numero presione enter""")
Menu()

def factorial():
  try:  
    num = int(input("Calcular factorial de: "))
    factorial = 1
  except:
    print("solo valores numericos")
    num = 0
    factorial()

  if num < 0:
     print("Sorry, factorial does not exist for negative numbers")
  elif num == 0:
     print("The factorial of 0 is 1")
  else:
     for i in range(1,num + 1):
        factorial = factorial*i
     print("The factorial of",num,"is",factorial)

factorial()
