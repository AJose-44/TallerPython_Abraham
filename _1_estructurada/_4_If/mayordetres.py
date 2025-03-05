if __name__ == '__main__':
    a=int(input("Proporciona un numero: "))
    b=int(input("Proporciona otro numero: "))
    c=int(input("Proporciona un último numero: "))

    if a>b:
        if a>c:
            print(f"El mayor es {a} ")
        else:
            print(f"El mayor es {b} ")
            """
            alt shift para moverle
            """
    else:
        if c>a:
            print(f"El mayor sería {c} ")
        else:
            print(f"El mayor sería {b} ")
