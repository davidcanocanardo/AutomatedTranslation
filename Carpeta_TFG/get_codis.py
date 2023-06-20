import os

#Guió encarregat de descarregar els fitxers de Zenodo
#Ús: Executa el guió, aleshores intercanvia el nom dels dos fitxers "taula" ("taula" <-> "_taula")

taula = open("taula", "r").read()
paraules = taula.split(" ")
tenen_href = [x for x in paraules if "href" in x]
llista_noms = []
for i in range(0, len(tenen_href),2):
    nom = tenen_href[i].split(">")[1][0:-3]
    llista_noms.append(nom)

while(len(llista_noms)>0):
    print(llista_noms[0])
    os.system("cd codis2; curl https://zenodo.org/record/4501622/files/" + llista_noms[0] + "?download=1 -o "+ llista_noms[0])
    llista_noms.pop(0)
    print("Falten " + str(len(llista_noms)) + " fitxers per descarregar")
