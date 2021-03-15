import psycopg2

def bisiesto():
  conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")


  año = int(input("inserte año a evaluar: "))
  cursor1=conexion.cursor()
  sql="insert into año(año, tipo) values (%s,%s)"
  if (año % 4 != 0): 
        print(año, " no es bisiesto")
        f = open('año.txt','a')
        f.write('\n'+ str(año) + " no es bisiesto")
        f.close()
        datos=(año, "no bisiesto")
        cursor1.execute(sql, datos)
  elif (año % 4 == 0 and año % 100 != 0): 
        print(año, " es bisiesto")
        f = open('año.txt','a')
        f.write('\n'+ str(año) + " es bisiesto")
        f.close()
        datos=(año, "bisiesto")
        cursor1.execute(sql, datos)
  elif (año % 4 == 0 and año % 100 == 0 and año % 400 != 0): 
        print(año, " no es bisiesto")
        f = open('año.txt','a')
        f.write('\n'+ str(año) + " no es bisiesto")
        f.close()
        datos=(año, "no bisiesto")
        cursor1.execute(sql, datos)
  elif (año % 4 == 0 and año % 100 == 0 and año % 400 == 0): 
        print(año, " es bisiesto")
        f = open('año.txt','a')
        f.write('\n'+ str(año) + " es bisiesto")
        f.close()
        datos=(año, "bisiesto")
        cursor1.execute(sql, datos)
  conexion.commit()
  conexion.close() 
bisiesto()
