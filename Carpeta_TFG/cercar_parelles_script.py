import os
from datetime import datetime

#Guió encarregat de buscar parelles de traduccions de Java a Kotlin.
#Ús: Crear un directori anomenat "codis2" on estan tots els projectes en format .zip
#    Executar el guió just fora del directori "codis2"

#*1 importing shutil module 
import shutil
print("_____________Llistant tots els codis_____________") 
file_list = os.listdir("codis2")
print("_____________Comença_____________") 
while len(file_list)>0:
    act_file = file_list[0]
    if (act_file[-4:]==".zip"):
        print("Hora actual =", datetime.now().strftime("%H:%M:%S"))#https://www.programiz.com/python-programming/datetime/current-time
        #*1--------https://www.studytonight.com/python-howtos/how-to-unzip-file-in-python-------------------
        # Path of the file
        filename = "./codis2/" + act_file

        # Target directory
        extract_dir = "./codis2"

        # Unzip the file 
        print("_____________UnZip del fitxer " + act_file + "_____________") 
        shutil.unpack_archive(filename, extract_dir)
        print("_____________BUSCANT MIGRACIONS A " + act_file[0:-4] + "_____________")
        os.system('java -cp ./miga-0.0.1-SNAPSHOT-jar-with-dependencies.jar fr.uphf.se.kotlinresearch.core.MigaMain ./dataset ./codis2/' + act_file[0:-4])
        print("_____________ELIMINANT: '" + act_file[0:-4] + "'_____________")      
        os.system('rm -rf ./codis2/' + act_file[0:-4])
        os.system('mv ./codis2/' + act_file + ' ./codis')
    file_list.pop(0)
    print("Queden " + str(len(file_list)) + " directoris per buscar")
    

