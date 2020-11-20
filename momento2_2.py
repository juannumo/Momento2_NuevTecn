# 2.	Escribir una función que cuente la cantidad de apariciones de cada carácter en una cadena de texto, y los devuelva en un diccionario.


from collections import defaultdict

texto2 = "esto es un ensayo para contar caracteres"

contador = defaultdict(int)

for c in texto2:
    if(c.isalpha()):
        contador[c] += 1

for c in sorted(contador, key=contador.get, reverse=True):
    if contador[c] > 2:
        # print(texto2.replace(' ',''))
        print('el caracter %s se repite %i' % (c, contador[c]))
        