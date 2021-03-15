import math
import psycopg2

def cuadrado(L):
    conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
    cursor1=conexion.cursor()
    sql="insert into areas(fig, area) values (%s,%s)"
    area=L**2
    f = open('areas.txt','a')
    f.write('\nlado' + str(L) + 'el area del cuadrado es: '+ str(area))
    f.close()
    datos=("cuadrado", area)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close() 
    return  print('el area del cuadrado es: ', area)

def circulo(R):
    conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
    cursor1=conexion.cursor()
    sql="insert into areas(fig, area) values (%s,%s)"
    area=math.pi*R**2
    f = open('areas.txt','a')
    f.write('\nRadio' + str(R) + 'el area del circulo es: '+ str(area))
    f.close()
    datos=("circulo", area)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close() 
    return print('el area del circulo es ', area)

def triangulo(b,h):
    conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
    cursor1=conexion.cursor()
    sql="insert into areas(fig, area) values (%s,%s)"
    area=b*h/2
    f = open('areas.txt','a')
    f.write('\nbase' + str(b) + 'altura' + str(h) + 'el area del triangulo es: '+ str(area))
    f.close()
    datos=("triangulo", area)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close() 
    return print('El area del triángulo es: ', area)

def rectangulo(b,h):
    conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
    cursor1=conexion.cursor()
    sql="insert into areas(fig, area) values (%s,%s)"
    area=b*h
    f = open('areas.txt','a')
    f.write('\nbase' + str(b) + 'altura' + str(h) + 'el area del rectangulo es: '+ str(area))
    f.close()
    datos=("rectangulo", area)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close() 
    return print('El area del Rectángulo es: ', area)

def calculadora():
  print("""calculadora de areas para:
         1.Cuadrado.
         2.Circulo.
         3.Triángulo.
         4.Rectángulo.
         otro para Salir
      ****************************""")

  x=int(input("Escoja la figura: "))

  if x==1:
      L=int(input('Ingrese el lado: '))
      cuadrado(L)
    
  elif x==2:
      R=int(input('Ingrese el radio del circulo: '))
      circulo(R)
    
  elif x==3:  
      b=int(input('Ingrese la base: '))
      h=int(input('Ingrese la altura: '))
      triangulo(b,h)
    
  elif x==4:
      b=int(input('Ingrese la base: '))
      h=int(input('Ingrese la altura: '))
      rectangulo(b,h)
  else:
      print("no saliendo calculadora")
calculadora()
