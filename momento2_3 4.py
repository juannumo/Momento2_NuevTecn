# 3.	Pide números y mételos en una lista, cuando el usuario meta un 0 ya dejaremos de insertar. Por último, muestra los números ordenados de menor a mayor.

listaNum = []
salir = False
while(not salir):
    numero = int(input("Escribe un numero: "))
    if(numero == 0):
        salir=True
    else:
        listaNum.append(numero)
listaNum.sort()
print(listaNum)

