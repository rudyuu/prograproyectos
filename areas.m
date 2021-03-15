  fprintf("calculadora de areas para:\n")
  fprintf("1.Cuadrado.\n")
  fprintf("2.Circulo.\n")
  fprintf("3.Triángulo.\n")
  fprintf("4.Rectángulo.\n")
  fprintf("otro para Salir\n")
  fprintf("****************************\n")
  x=input("Escoja la figura: ")

  fid = fopen('areas.txt','a');
  if x==1
      L=input('Ingrese el lado: ')
      area=L**2
      fprintf('el area del cuadrado es: %d', area)
      fprintf(fid,"\nCuadrado de lado %d tiene de area %d",L,area)
    
  elseif x==2
      R=input('Ingrese el radio del circulo: ')
      area=pi*R*R
      fprintf('el area del circulo es %d', area)
      fprintf(fid,"\nCirculo de radio %d tiene de area %d",R,area)
    
  elseif x==3  
      b=input('Ingrese la base: ')
      h=input('Ingrese la altura: ')
      area=b*h/2
      fprintf('El area del triángulo es: %d', area)
      fprintf(fid,"\nTriangulo de base %d y altura %d tiene de area %d",b,h,area)
    
  elseif x==4
      b=input('Ingrese la base: ')
      h=input('Ingrese la altura: ')
      area=b*h
      fprintf('El area del Rectángulo es: %d', area)
      fprintf(fid,"\nRectangulo de base %d y altura %d tiene de area %d",b,h,area)
  else
      fprintf("saliendo calculadora")
  end
  fclose(fid)