# 4.	Hacer una actividad que pida al usuario escribir una cantidad X de nombres de personas (puede hacerlo con el ciclo que considere). Después el sistema deberá demostrar cuales son los nombres que empiezan con la letra "C" sea minúscula o mayúscula.


listaNom = []
listaNomC = []
for i in range(0,5):
    nombre = input("Ingrese el nombre de una persona: ")
    listaNom += [nombre]

print(listaNom)

for nom in listaNom:
    if nom[0] == 'c' or nom[0] == 'C':
        listaNomC += [nom]

print(listaNomC)

