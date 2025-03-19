def suma(a:int,b:int)->int:
    return a+b

def sumaArreglo(lista:list)->int:
    return sum(lista)

if __name__ == '__main__':
    print(f"La suma es: {suma(11,22)}")
    lista=[11,12,13,14,15,16,17,18,19,20,21,22]
    print(f"La suma es: {sumaArreglo(lista)}")