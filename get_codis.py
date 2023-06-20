import os

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
#os.system("cd codis; curl https://zenodo.org/record/4463389/files/ai-susi.zip?download=1 -o ai-susi.zip")
#os.system("cd codis; curl https://zenodo.org/record/4463389/files/app-simone.zip?download=1 -o app-simone.zip")
