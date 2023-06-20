import os
#import git
from datetime import datetime


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
        #---------------------------------------------------------------------------------------------------
        #os.system('cd ./codis/' + act_file[0:-4])
        #os.system('git fetch')
        #os.system('cd ../..')
        #g = git.Repo("./codis/" + act_file[0:-4])
        #print("_____________FETCHING: '" + act_file[0:-4] + "'_____________")  
        #if g.is_dirty(untracked_files=True):
        #    print('Changes detected.')
        #    g.git.stash('save')
        #    g.remotes.origin.pull()
        #g.remotes.pull()
        print("_____________BUSCANT MIGRACIONS A " + act_file[0:-4] + "_____________")
        os.system('java -cp ./miga-0.0.1-SNAPSHOT-jar-with-dependencies.jar fr.uphf.se.kotlinresearch.core.MigaMain ./dataset ./codis2/' + act_file[0:-4])
        print("_____________ELIMINANT: '" + act_file[0:-4] + "'_____________")      
        os.system('rm -rf ./codis2/' + act_file[0:-4])
        os.system('mv ./codis2/' + act_file + ' ./codis')
    file_list.pop(0)
    print("Queden " + str(len(file_list)) + " directoris per buscar")
    

