  x = input("sumar hasta ")
  n = 0
  z = x
  fid = fopen('sumanums.txt','a');
  fprintf(fid,"\nSuma 0 hasta %d =",x)
  while (n + 1) < z
      x = x + (n + 1)
      n = n + 1
  endwhile
  fprintf("el resultado de la suma es: %d", x)
  fprintf(fid," %d ",x)
  fclose(fid)