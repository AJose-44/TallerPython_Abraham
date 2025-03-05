if __name__ == '__main__':
    a=str(input("Proporciona un nombre "))
    b=str(input("Proporciona un segundo nombre "))

    n1 = len(a)
    n2 = len(b)

    if n1>n2:
        print(f"El más largo es {a} ")
    else:
        if n1==n2:
            print(f"Los nombres {a} y {b} son iguales ")
        else:
            print(f"El más largo es {b} ")
