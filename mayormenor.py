import psycopg2

print ('Programa para la resolución del máximo de cinco números.')
print ('Escribe cero(0), para salir.')
while True:
  try:
   a = int(input('Escribe el primer numero: '))
   b = int(input('Escribe el segundo numero: '))
   c = int(input('Escribe el tercer numero: '))
   d = int(input('Escribe el cuarto numero: '))
   e = int(input('Escribe el quinto numero: '))
  except ValueError:
    print ("No puedes dejar la entrada en blanco, ni escribir letras")
    a=0
  if a==0:
   print("saliendo")
   break
  if a > b and a > c and a > d and a > e:
   mayor = a
  elif b > a and b > c and b > d and b > e:
   mayor = b
  elif c > a and c > b and c > d and c > e:
   mayor = c
  elif d > a and d > b and d > c and d > e:
   mayor = d
  else:
   mayor = e

  if a < b and a < c and a < d and a < e:
   menor = a
  elif b > a and b < c and b < d and b < e:
   menor = b
  elif c < a and c < b and c < d and c < e:
   menor = c
  elif d < a and d < b and d < c and d < e:
   menor = d
  else:
   menor = e
  print ('El mayor es: ', mayor)
  print ('El menor es: ', menor)
  #base de datos
  conexion = psycopg2.connect(host="localhost", database="parcial", user="postgres")
  cursor1=conexion.cursor()
  sql="insert into numeros(mayor, menor) values (%s,%s)"
  datos=(mayor, menor)
  cursor1.execute(sql, datos)
  conexion.commit()
  conexion.close()
  #archivo txt
  f = open('mayormenor.txt','a')
  f.write('\nEl mayor: ' + str(mayor) + 'El menor: ' + str(menor))
  f.close()
  
  

