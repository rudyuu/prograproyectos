  ano = input("inserte año a evaluar: ")
  m1 = mod(ano,4);
  m2 = mod(ano,100);
  m3 = mod(ano,400);
  fid = fopen('bisiesto.txt','a');
  if (m1 != 0)
        fprintf("%d no es bisiesto\n",ano)
        fprintf(fid,"%d no es bisiesto\n",ano)
  elseif (m1 == 0 )&( m2 != 0) 
        fprintf("%d es bisiesto\n",ano)
        fprintf(fid,"%d es bisiesto\n",ano)
  elseif (m1 == 0 )&( m2 == 0 )&( m3 != 0) 
        fprintf("%d no es bisiesto\n",ano)
        fprintf(fid,"%d no es bisiesto\n",ano)
  elseif (m1 == 0 )&( m2 == 0 )&( m3 == 0) 
        fprintf("%d es bisiesto\n",ano)
        fprintf(fid,"%d es bisiesto\n",ano)
  end
  fclose(fid)