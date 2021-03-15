  num = input("introducir numero ")
  fprintf("divisores de %d",num)
  fid = fopen('divisores.txt','a');
  fprintf(fid,"\ndivisores de %d: ",num)
  for divisor=1:num+1
      m = mod(num,divisor)
      if (m == 0) 
            disp(divisor)
              fprintf(fid,"%d, ",divisor)          
      end
  endfor  
  fclose(fid)
  