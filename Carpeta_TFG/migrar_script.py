import os
                
#Guió encarregat de preparar les migracions per IntellIJ         
                
def funcio(path_act):
    dir_list = os.listdir(path_act)
    cont = 0
    while len(dir_list)>cont:
        act_dir = dir_list[cont]
        #-----------https://www.w3resource.com/python-exercises/python-basic-exercise-85.php---------------- cerca si és un directori
        if (os.path.isdir("./" + path_act + "/" + act_dir)):
            print("------------Entrant a  " + act_dir + "------------")
            funcio(path_act + "/" + act_dir)
        elif act_dir[-5:]==".java":
            if (dir_list.count(act_dir[0:-5] + "_PRIMA.kt")==0):
                nom = path_act.replace("/","&")

                os.system('cp ./' + path_act + '/' + act_dir + ' ./codis_per_migrar/' + nom + "&" + act_dir)#migrar codi
        cont += 1
    print("############Sortint de " + path_act.split("/")[-1] + "############")
    
path="dataset"
funcio(path)
