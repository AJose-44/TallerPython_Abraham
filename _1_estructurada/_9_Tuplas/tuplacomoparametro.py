
    #función que recibe una tupla y la desempaqueta
def calcular_area(rectangulo: tuple[int, int])-> int:
        largo, ancho = rectangulo
        return largo * ancho

def cuadrado(rectangulo: tuple[int, int])-> tuple[int,int]:
    largo, ancho = rectangulo
    largo = largo * ancho
    ancho = ancho * largo
    return (largo, ancho)

if __name__ == '__main__':
    #crear la tupla
    dimensiones =(10, 5)

    #llamar la función con la tupla
    area = calcular_area(dimensiones)
    print(f"El área del rectangulo es: {area} mts. cuadrados")

    largo, ancho = cuadrado((5,3))
