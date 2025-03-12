if __name__ == '__main__':
    print("________________")
    lista=[1,2,3,"Lunes",4,5,6,7,8,9,10,11,12,13,14,15,16]
    #Una lista puede contener valores de diferente tipo
    #Además una lista es mutable

    #for elemento in lista:
    #    print(elemto)

    lista.append(200)
    lista.append("Viernes")
    lista.append(False)
    lista.append(2.69)
    lista.append(-100)

    lista2=[1200,1300,1500]

    lista.append(lista2)

    for elemento in lista:
        print(elemento)

    nombre:str
    nombre="Luis"
    nombre +="Gutierrez"
    nombre.join("Gutierrez")
    print(nombre)

    lista3=["Federico", "Pablo", "Karla"]
    cadena:str=" - ".join(lista3)#La función join se utiliza para contatenar
    print(cadena)

    separado=cadena.split()#Split se utiliza para seprar los elementos
    for dato in separado:
        print(dato)
    