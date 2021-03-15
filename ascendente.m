num1 = input("inicial ")
num2 = input("final ")
fid = fopen('ascendente.txt','a');       
if (num1 < num2)
  fprintf(fid,"\nDe %d a %d: ",num1,num2) 
  while (num1 <= num2)
     disp(num1)
     fprintf(fid,"%d, ",num1) 
     num1 = num1 +2
  endwhile
else
fprintf("el primer numero debe ser menor")
end
fclose(fid)