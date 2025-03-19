if __name__ == '__main__':
    #añade un elemento al final de la lista
    mi_lista=[1,2,3]
    mi_lista.append(4)
    print(mi_lista)

    #añade los elementos a la lista
    mi_lista=[1,2,3]
    otra_lista=[4,5,6]
    mi_lista.extend(otra_lista)
    print(mi_lista)

    #inserta un elemento en una posición especial
    mi_lista=[1,2,3]
    mi_lista.insert(1,4)
    print(mi_lista)

    #elimina el primer elemento de la lista
    mi_lista=[1,2,3]
    mi_lista.remove(2)
    print(mi_lista)

    #elimina y devuelve el elemento en una posición específica
    mi_lista=[1,2,3]
    elemento=mi_lista.pop(1)
    print(elemento)
    print(mi_lista)

    #devuelve el índice de la primera aparición de un elemento en la lista
    mi_lista=[1,2,3,2]
    indice=mi_lista.index(2)
    print(indice)

    #devuelve el número de veces que aparaece un elemento en la lista
    mi_lista=[1,2,3,2]
    conteo=mi_lista.count(2)
    print(conteo)

    #ordena los elementos de la lista de forma asimentrica
    mi_lista=[3,1,4,2]
    mi_lista.sort()
    print(mi_lista)

    mi_lista.sort(reverse=True)
    print(mi_lista)

    #invierte el orden de los elementos de la lista
    mi_lista=[1,2,3,4]
    mi_lista.reverse()

    #elimina todos los elementos de la lista
    mi_lista=[1,2,3]
    mi_lista.clear()
    print(mi_lista)

    #devuelve una copia superficial de la lista
    mi_lista=[1,2,3]
    mi_lista2=mi_lista
    copia_lista=mi_lista.copy()
    mi_lista.append(4)

    #print(copia_lista)
    print(mi_lista2)