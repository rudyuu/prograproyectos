def calculo():
  num = int(input("introducir numero "))
  f = open('divisores.txt','a')
  print("divisores de ",num)
  f.write("\ndivisores de " + str(num))
  for divisor in range(1,num+1):
      if (num % divisor) == 0 :
          print(divisor)
          f.write("\n" + str(divisor))
  f.close()
         
calculo()
