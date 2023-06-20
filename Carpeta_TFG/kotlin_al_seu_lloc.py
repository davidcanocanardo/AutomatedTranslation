import os

#Guió encarregat de retornar els codis migrats al seu directori

dir_list = os.listdir("codis_migrats")

while len(dir_list)>0:
    nom = dir_list[0].replace("&","/")
    os.system('mv ./codis_migrats/' + dir_list[0] + ' ./' + nom[0:-3] + "_PRIMA.kt")#migrar codi
    dir_list.pop(0)
    print(len(dir_list))
