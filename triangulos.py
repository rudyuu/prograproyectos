import psycopg2

while True:
  print("""\nA continuacion ingresara los tres lados de un triangulo""")
  try: 
   lado1 = int(input("ingrasar lado 1: "))
   lado2 = int(input("ingrasar lado 2: "))
   lado3 = int(input("ingrasar lado 3: "))
  except ValueError:
   print ("No puedes dejar la entrada en blanco, ni escribir letras")
   break

  conexion = psycopg2.connect(host="localhost", database="parcial", user="postgres")
  cursor1=conexion.cursor()
  sql="insert into triangulo(lado1, lado2, lado3, tipo) values (%s,%s,%s,%s)"

  f = open('triangulos.txt','a')
  f.write('\n'+str(lado1)+' '+ str(lado2)+' '+ str(lado3))
  if (lado1 == lado2 and lado2 == lado3):
    print("el triangulo es equilatero")
    f.write("\nel triangulo es equilatero")
    datos=(lado1,lado2,lado3, 'equilatero')
  elif (lado1 == lado2 or lado2 == lado3 or lado1 == lado3):
    print("el triangulo es isosceles")
    f.write("\nel triangulo es isosceles")
    datos=(lado1,lado2,lado3, 'isosceles')
  else:
    print("el triangulo es escaleno")
    f.write("\nel triangulo es escaleno")
    datos=(lado1,lado2,lado3, 'escaleno')

  f.close()
  cursor1.execute(sql, datos)
  conexion.commit()
  conexion.close()






