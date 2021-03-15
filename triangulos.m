  fprintf("A continuacion ingresara los tres lados de un triangulo\n")
  lado1 = input("ingrasar lado 1: ")
  lado2 = input("ingrasar lado 2: ")
  lado3 = input("ingrasar lado 3: ")
  fid = fopen('triangulos.txt','a');
  fprintf(fid,"\nLados: %d %d %d ",lado1,lado2,lado3) 
  if (lado1 == lado2) & (lado2 == lado3)
    fprintf("el triangulo es equilatero\n")
    fprintf(fid," el triangulo es equilatero")
  elseif (lado1 == lado2) | (lado2 == lado3) | (lado1 == lado3)
    fprintf("el triangulo es isosceles\n")
    fprintf(fid," el triangulo es isosceles")
  else
    fprintf("el triangulo es escaleno\n")
    fprintf(fid," el triangulo es escaleno")
  end
  fclose(fid)