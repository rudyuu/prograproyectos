disp("\n____Ingrese un número entero, positivo y divisible entre 7 para calcular su factorial___\n")

while true
  try
   x = int32(input("\nfactorial de: "));
  catch
   disp("ingrese un valor numerico")
   fid = fopen('factorsiete.txt','a');
   fprintf(fid,"\nel valor no era valido")
   fclose(fid)
   disp("\n____Ingrese un número entero y positivo para calcular su factorial___\n")
   x = int32(input("\nfactorial de: "));
  end_try_catch
 

  n = 0
  z = x
  m = mod(x,7)
  if m == 0
    while ((n + 1) < z)
        x = x * (n + 1)
        n = n + 1
    endwhile
  
    if x == 0
        disp("El resultado de 0! es 1")
        fid = fopen('factorsiete.txt','a');
        fprintf(fid,"\nEl resultado de 0! es 1")
        fclose(fid)      
    elseif x < 0
        disp("No existe factorial de negativos")
        fid = fopen('factorsiete.txt','a');
        fprintf(fid,"\nNo existe factorial de negativos")
        fclose(fid)      
    else
        printf("El resultado de %d! es %d\n",z,x) 
        fid = fopen('factorsiete.txt','a');
        fprintf(fid,"\nEl resultado de %d! es %d",z,x)
        fclose(fid)
    end
  else
    fprintf("el numero no es divisible entre 7\n")
  end
end