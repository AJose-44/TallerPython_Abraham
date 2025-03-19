import statistics as mate

if __name__ == '__main__':
    numeros=[10,20,50,80,90,30,40]

    conteo=0
    suma=0
    promedio=0
    for valor in numeros:
        suma+=valor
        conteo+=1

    promedio=suma/conteo
    print(promedio)

    #opción medio lenta
    suma=0
    for valor in numeros:
        suma+=valor
    promedio=suma/len(numeros)
    print(promedio)

    #opción rápida
    promedio== mate.mean(numeros)
    print(promedio)
    """
    Mean es una función para promedio
    """