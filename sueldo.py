import psycopg2

print ('Programa para calcular el sueldo de una persona\n')
while True:
 try:
  hs=int(input("Ingrese las horas trabajadas: "))
 except ValueError:
  print ("No puedes dejar la entrada en blanco, ni escribir letras")
  break
 phs=50
 extras=(hs - 40)
 
 if hs<=40 and hs>0:
    sueldot=hs*phs
    print("su sueldo es: ",sueldot, " quetzales,")
    print(" no posee horas extras")
 elif hs>40:
    sueldo1=(extras*75)
    sueldo=hs*phs
    sueldot=sueldo+sueldo1
    print ("Su sueldo es: ",sueldo," quetzales\n")
    print ("El sueldo de sus horas extras es: ",sueldo1," quetzales\n")
    print ("Su sueldo total es ",sueldot," quetzales")
 else:
    print ("Las horas no pueden ser negativas")
  #base de datos
 conexion = psycopg2.connect(host="localhost", database="parcial", user="postgres")
 cursor1=conexion.cursor()
 sql="insert into sueldo(horas, extras, sueldo) values (%s,%s,%s)"
 datos=(hs, extras, sueldot)
 cursor1.execute(sql, datos)
 conexion.commit()
 conexion.close()
  #archivo txt
 f = open('sueldo.txt','a')
 f.write('\nTrabajo ' + str(hs) + 'hr su sueldo es: ' + str(sueldot) + 'quetzales')
 f.close()
