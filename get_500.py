import os
dir_list = os.listdir("codis_per_migrar")
cont = 0
while len(dir_list)>cont and cont<250:
    os.system("mv ./codis_per_migrar/" + dir_list[cont] + " ./codis_migrar_ara/codis")
    cont+=1     
