if __name__ == '__main__':
    #usar una tupla como clave en un diccionario
    diccionario = {
       ## ("id","int"):'2',
       ## 'nombre':'Juan',
      ##  'apellido':'Gutierrez'
    }
    #en los diccionarios no existen posiciones

    #agregar tupla como clave
    diccionario[("Ana",25)]="Estudiante"
    diccionario[("Luis",30)]="Ingeniero"
    diccionario[("Carlos", 40)]="Abogado"

    #acceder a los valores del diccionario usando la tupla
    ocupacion_ana=diccionario[("Ana",25)]
    ocupacion_luis=diccionario[("Luis",30)]

    print(f"Ana es: {ocupacion_ana}")
    print(f"Luis es: {ocupacion_luis}")
