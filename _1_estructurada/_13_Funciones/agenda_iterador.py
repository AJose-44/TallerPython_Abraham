def extraer(agenda: tuple):
    i:int=0
    while(i<len(agenda)):
        nombre,correo,tel = agenda[i]
        i+=1
        yield (nombre,correo,tel)

if __name__ == '__main__':
    agenda=[]
    agenda.append(("Juan","juan1@gmail.com","212586985"))
    agenda.append(("Jose","juan2@gmail.com","222586985"))
    agenda.append(("Juanes","juan3@gmail.com","232586985"))
    agenda.append(("Joan","juan4@gmail.com","242586985"))
    agenda.append(("John","juan5@gmail.com","252586985"))
    agenda.append(("Julian","juan6@gmail.com","262586985"))
    agenda.append(("Josexo","juan7@gmail.com","272586985"))
    agenda.append(("Josh","juan8@gmail.com","282586985"))
    agenda.append(("Juan2","juan9@gmail.com","292586985"))
    agenda.append(("Juan3","juan10@gmail.com","222186985"))

    for a,b,c in extraer(agenda):
        print(a,b,c)