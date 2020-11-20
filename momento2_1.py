# 1.	Escribir una función que reciba una cadena y devuelva un diccionario con la cantidad de apariciones de cada palabra en la cadena. Por ejemplo, si recibe "Qué lindo día que hace hoy" debe devolver: 'que': 2, 'lindo': 1, 'día': 1, 'hace': 1, 'hoy': 1


from collections import Counter


texto = 'Qué lindo día que hace hoy'

caracteres = {",", ".", "á", "é", "í", "ó", "ú", "ü"}
texto = texto.lower()

texto = texto.replace(",", "")
texto = texto.replace(".", "")
texto = texto.replace(":", "")
texto = texto.replace("á", "a")
texto = texto.replace("é", "e")
texto = texto.replace("í", "i")
texto = texto.replace("ó", "o")
texto = texto.replace("ú", "u")
texto = texto.replace("ü", "u")

palabras = texto.split()

contador = Counter(palabras)
frecuencia_palabra = [palabras.count(palabra) for palabra in palabras]

res={}
for key in palabras:
    for value in frecuencia_palabra:
        res[key] = value
        frecuencia_palabra.remove(value)
        break

print('número de veces que se repiten las palabras:')
print(res)


