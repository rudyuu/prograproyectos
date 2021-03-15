import psycopg2

def mantenimiento():
  print("sistema para mantenimiento del taxy\n")
  mod = int(input("ingrese el año de su vehiculo: "))
  km = int(input("Kilometros recorridos por su vehiculo: "))
  
  f = open('carro.txt','a')
  conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
  cursor1=conexion.cursor()
  sql="insert into carro(año,kilometros,situacion) values (%s,%s,%s)"
  if (mod < 2007 and km > 20):
   print("debe renovarse el auto")
   f.write('\naño: '+ str(mod)+ ' km: '+ str(km) + "debe renovarse el auto")
   datos=(mod, km, "renovarse")
   cursor1.execute(sql, datos)
    
  elif (mod >= 2007 and mod <= 2013 and km > 20000):
   print("debe recibir mantenimiento")
   f.write('\naño: '+ str(mod)+ ' km: '+ str(km) + "debe recibir mantenimiento")
   datos=(mod, km, "mantenimiento")
   cursor1.execute(sql, datos)

  elif (mod > 2013 and km < 10000):
   print("el auto esta en optimas condiciones")
   f.write('\naño: '+ str(mod)+ ' km: '+ str(km) + "el auto esta en optimas condiciones")
   datos=(mod, km, "optimo")
   cursor1.execute(sql, datos)

  else:
   print("llevar al mecanico")
   f.write('\naño: '+ str(mod)+ ' km: '+ str(km) + "llevar al mecanico")
   datos=(mod, km, "al mecanico")
   cursor1.execute(sql, datos)
  conexion.commit()
  conexion.close()
  f.close()
mantenimiento()
