import os
dir_list = os.listdir("codis_migrar_ara/codis")
while len(dir_list)>0:
    os.system("mv ./codis_migrar_ara/codis/" + dir_list[0] + " ./codis_migrats")
    dir_list.pop(0)     