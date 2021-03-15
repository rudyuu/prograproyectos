import psycopg2

def main():
   num1 = 1
   num2 = 100
   contador = 0
   f = open('impares.txt','a')
   conexion = psycopg2.connect(host="localhost", database="tarea", user="postgres")
   sql="insert into impares(impares,cantidad) values (%s,%s)"
   cursor1=conexion.cursor()
   for i in range(num1, num2):
        if i % 2 != 0:
           print(i)
           contador+=1
           f.write('\n' + str(i))
           datos=(i,contador)
           cursor1.execute(sql, datos)
            
   print("del 1 al 100 se contaron ", contador, " impares")
   f.write('\n' + "del 1 al 100 se contaron "+ str(contador) + " impares")
   f.close()
   sql="insert into impares(cantidad) values (%s)"
   conexion.commit()
   conexion.close()
main()
