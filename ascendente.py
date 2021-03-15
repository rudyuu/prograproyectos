import psycopg2

def calculo():
   num1 = int(input("inicial "))
   num2 = int(input("final "))
   conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
   cursor1=conexion.cursor()
   sql="insert into ascendente(inicio, final) values (%s,%s)"
   if num1 < num2:
    datos=(num1, num2)
    cursor1.execute(sql, datos)
    conexion.commit()
    conexion.close() 
    while num1 <= num2:
       print(num1)
       f = open('ascendente.txt','a')
       f.write('\n'+ str(num1))
       f.close()
       num1 = num1 +2
   else:
    print("el primer numero debe ser menor")
    f = open('ascendente.txt','a')
    f.write('\n'+ "el primer numero debe ser menor")
    f.close()
calculo()
