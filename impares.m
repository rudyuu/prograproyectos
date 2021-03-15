   num1 = 1
   num2 = 100
   contador = 0
   fid = fopen('impares.txt','a');
   for i = num1:num2
     m = mod(i,2)
        if m != 0
           fprintf("%d es impar, entonces ", i)
           fprintf(fid,"%d, ", i)
           contador+=1
        end
   endfor
   fprintf("del 1 al 100 se contaron %d impares", contador)
   fprintf(fid,"\ndel 1 al 100 se contaron %d impares", contador)
   fclose(fid)