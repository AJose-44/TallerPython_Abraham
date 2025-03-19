import statistics as mate
##def suma(a:int, b):
  ##  print(f"La suma de {a} + {b} es: {a+b}")

def suma(a:int, b:None, c=None):
    if b is None:
        print(f"{a}")
    if c is None:
        print(f"La suma de {a} + {b} es {a + b}")
    else:
        print(f"La suma de {a} + {b} + {c} es: {a + b + c}")

def promedioArreglo(lista):
    lista.append(5)
    lista.append(45)
    lista.append(56)
    p=mate.mean(lista)
    print(f"El promedio es {p}")

if __name__ == '__main__':
    suma(10,52)
    suma(23,47,44)
    suma(12,255)

    lista2=[1,2,3,4,5]
    #La lista saldrá del método alterada
    #lista2=lista1
    promedioArreglo(lista2)
    print(lista2)