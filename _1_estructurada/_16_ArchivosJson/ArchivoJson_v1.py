import json

if __name__ == '__main__':
    #Versión corta de abrir un archivo JSON
    #Abre el archivo JSON en modo de lectura y with se encarga de cerrar
    with open("datos.json", "r", encoding="utf-8") as archivo:      #carga el contenido del archivoa JSON
        datos = json.load(archivo)

    #Muestra el contenido JSON
    for persona in datos["Personas"]:
        print("Nombre:", persona["nombre"])
        print("Edad:", persona["edad"])
        print("Ciudad:", persona["ciudad"])
        print("Estado:", persona["estado"])
        print("-------------------") #Línea en blanco para separar