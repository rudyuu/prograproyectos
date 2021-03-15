   num1 = input("inserte un numero: ")
   num2 = input("inserte otro numero: ")

   fid = fopen('descendente.txt','a');
   if (num1 < num2)
     x = num2
     y = num1
   else
     x = num1
     y = num2
   end
   fprintf(fid,"\nde %d a %d: ",x,y)
   while (x >= y)
       disp(x)
       fprintf(fid,"%d, ",x)
       x = x - 1
   endwhile
   fclose(fid)