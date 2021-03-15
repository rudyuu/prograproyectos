import psycopg2

def calculadora():
  print("""A continuacion ingresara las notas de un estudiante""")
  n1 = int(input("Nota 1er parcial: "))
  n2 = int(input("Nota 2do parcial: "))
  n3 = int(input("Nota 3er parcial: "))

  f = open('promedio.txt','a')
  f.write('\n'+str(n1)+' '+str(n2)+' '+str(n3)+' ')
  prom = ((n1+n2+n3)/3)
  conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
  cursor1=conexion.cursor()
  sql="insert into notas(n1,n2,n3,final) values (%s,%s,%s,%s)"
  if (prom < 60):
    print("su nota es de ", prom, "reprueba")
    f.write("\nsu nota es de "+ str(prom)+ " reprueba")
    datos=(n1,n2,n3,"reprueba")
    cursor1.execute(sql, datos)
  else:
    print("su nota es de ", prom, "aprueba")
    f.write("\nsu nota es de "+ str(prom)+ " aprueba")
    datos=(n1,n2,n3,"aprueba")
    cursor1.execute(sql, datos)
  f.close()
  conexion.commit()
  conexion.close() 
calculadora()
