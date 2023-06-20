import os

#Guió encarregat de posar 500 codis a la carpeta ./codis_migrar_ara/codis per tal de migrar-los

dir_list = os.listdir("codis_per_migrar")
cont = 0
while len(dir_list)>cont and cont<500:
    if(dir_list[cont].count(".kt") == 0):
        os.system("mv ./codis_per_migrar/" + dir_list[cont] + " ./codis_migrar_ara/codis")
        cont+=1     
