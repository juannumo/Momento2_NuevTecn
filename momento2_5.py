# 5.	Realice una FUNCIÓN en Python que calcule el índice de masa corporal de una persona y diga el estado en que se encuentre. Debe recibir los parámetros necesarios.

intro = """ 
Calculadora del Índice de Masa Corporal (IMC) para adultos
Sistema métrico: Kilogramos y metros
Sistema inglés: Pies, pulgadas y libras

¡¡Escriba los valores de acuerdo al sistema que maneje!!

"""

def estado(masaCorp):
    if masaCorp < 18.5:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Peso insuficiente")

    if masaCorp >= 18.5 and masaCorp < 24.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Normopeso")

    if masaCorp >= 25 and masaCorp < 26.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Sobrepeso grado I")

    if masaCorp >= 27 and masaCorp < 24.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Sobrepeso grado II 'Preobesidad'")

    if masaCorp >= 30 and masaCorp < 34.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Peso insuficiente")

    if masaCorp >= 35 and masaCorp < 39.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Peso insuficiente")

    if masaCorp >= 40 and masaCorp < 49.9:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Peso insuficiente")
        
    if masaCorp > 50:
        print("y según los parámetros definidos, su IMC es: ", masaCorp)
        print("Su clasificación es: Obesidad de tipo IV 'Extrema'")


def masaCorporal(em, epi, epu, pk, pl):   
    if pk > 0:        
        if em > 0:            
            masaCorpkm = pk / (em * em)
            print("Siguiendo el Sistema Métrico")
            estado(masaCorpkm)

    else:
        print("No hay suficiente información para dar una respuesta Siguiendo el Sistema Métrico")

    if pl > 0:        
        if epi > 0:
            pl = pl/2.20462
            epi = epi/3.28084           
            masaCorpkm = pl / (epi * epi)
            print("Siguiendo el Sistema Inglés con pies")
            estado(masaCorpkm)

        if epu > 0:
            pl = pl/2.20462
            epu = epu/39.3701           
            masaCorpkm = pk / (em * em)
            print("Siguiendo el Sistema Inglés con pulgadas")
            estado(masaCorpkm) 


    else:
        print("No hay suficiente información para dar una respuesta Siguiendo el Sistema Inglés")   

print(intro)

pk = (input("Ingrese su peso en Kilogramos:")) 
pl = (input("Ingrese su peso en Libras:")) 
em = (input("Ingrese su estatura en Metros: ")) 
epi = (input("Ingrese su estatura en Pies: ")) 
epu = (input("Ingrese su estatura en Pulgadas: ")) 

if pk == "":
    pk=0
else:
    pk=float(pk)

if pl == "":
    pl=0
else:
    pl=float(pl)

if em == "":
    em=0
else:
    em=float(em)

if epi == "":
    epi=0
else:
    epi=float(epi)

if epu == "":
    epu=0
else:
    epu=float(epu)

masaCorporal(em, epi, epu, pk, pl)







