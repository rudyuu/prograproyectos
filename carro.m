  fprintf("sistema para mantenimiento del taxy\n")
  modelo = input("ingrese el año de su vehiculo: ")
  km = input("Kilometros recorridos por su vehiculo: ")

  fid = fopen('carro.txt','a');
  fprintf(fid,"\nmodelo: %d  con %d km",modelo,km)

  if (modelo < 2007 )&( km > 20)
   fprintf("debe renovarse el auto\n")
   fprintf(fid," debe renovarse el auto")
  elseif (modelo >= 2007 )&( modelo <= 2013 )&( km > 20000)
   fprintf("debe recibir mantenimiento\n")
   fprintf(fid," debe recibir mantenimiento")
  elseif (modelo > 2013 )&( km < 10000)
   fprintf("el auto esta en optimas condiciones\n")
   fprintf(fid," el auto esta en optimas condiciones")
  else
   fprintf("llevar al mecanico\n")
   fprintf(fid," llevar al mecanico")
  end
  fclose(fid) 