  fprintf("A continuacion ingresara las notas de un estudiante\n")
  n1 = input("Nota 1er parcial: ")
  n2 = input("Nota 2do parcial: ")
  n3 = input("Nota 3er parcial: ")

  prom = ((n1+n2+n3)/3)
  fid = fopen('promedio.txt','a');
  fprintf(fid,"\n notas: %d. %d. %d. promedio: %d ",n1,n2,n3,prom)
  if (prom < 60)
    fprintf("su nota es de %d reprueba\n", prom)
    fprintf(fid, "REPROBADO")    
  else
    fprintf("su nota es de %d aprueba\n", prom)
    fprintf(fid, "APROBADO")
  end
  fclose(fid)