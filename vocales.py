def main():
   cadena = input("ingrese una palabra: ")
   cadena = cadena.lower()
   contador = 0
   for cad in cadena:
        if cad in "aeiou":
            contador += 1
   print('\nCantidad de vocaless: ',contador)
   f = open('vocales.txt','a')
   f.write('\nCantidad de vocaless: '+ str(contador))
   f.close()
main()
