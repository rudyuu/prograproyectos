def main():
   cadena = input("ingrese una palabra: ")
   cadena = cadena.lower()
   a = 0
   e = 0
   i = 0
   o = 0
   u = 0
   for cad in cadena:
        if cad in "a":
            a += 1
        if cad in "e":
            e += 1
        if cad in "i":
            i += 1
        if cad in "o":
            o += 1
        if cad in "u":
            u += 1
   f = open('cadavocal.txt','a')
   print('\nCantidad de As: ',a)
   f.write('\nCantidad de As: ' + str(a))
   print('\nCantidad de Es: ',e)
   f.write('\nCantidad de Es: ' + str(e))
   print('\nCantidad de Is: ',i)
   f.write('\nCantidad de Is: ' + str(i))
   print('\nCantidad de Os: ',o)
   f.write('\nCantidad de Os: ' + str(o))
   print('\nCantidad de Us: ',u)
   f.write('\nCantidad de Us: ' + str(u))
   f.close()
main()
