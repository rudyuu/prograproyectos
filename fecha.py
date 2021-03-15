from datetime import datetime
from dateutil.relativedelta import relativedelta
import psycopg2

while True:
 try: 
  a = int(input('Escribe dia de nacimiento: '))
  b = int(input('Escribe mes de nacimiento: '))
  c = int(input('Escribe año de nacimiento: '))
 except ValueError:
  print ("No puedes dejar la entrada en blanco, ni escribir letras")
  break
 nac = a , b ,c
 edad = relativedelta(datetime.now(), datetime(c, b, a))
 print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
 #base de datos
 conexion = psycopg2.connect(host="localhost", database="parcial", user="postgres")
 cursor1=conexion.cursor()
 sql="insert into edad(nacimiento, edad) values (%s,%s)"
 conv = str(edad.years), str(edad.months),str(edad.days)
 datos=(nac, conv)
 cursor1.execute(sql, datos)
 conexion.commit()
 conexion.close()
 #archivo txt
 f = open('edad.txt','a')
 f.write('\nNacio el ' + str(a) + "/" + str(b)+ "/" + str(c) + ' su edad es: '+ str(edad.years) + " años " + str(edad.months) + " meses " + str(edad.days) + " dias ")
 f.close()
