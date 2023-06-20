import os
                
def funcio(path_act):
    dir_list = os.listdir(path_act)
    while len(dir_list)>0:
        act_dir = dir_list[0]
        #-----------https://www.w3resource.com/python-exercises/python-basic-exercise-85.php---------------- cerca si és un directori
        if (os.path.isdir("./" + path_act + "/" + act_dir)):
            print("------------Entrant a  " + act_dir + "------------")
            funcio(path_act + "/" + act_dir)
        elif act_dir[-5:]==".java":
            #os.system('cp ' + act_dir[0:-4] + ' ./codis_per_migrar')
            os.system('cp ./' + path_act + '/' + act_dir + ' ./codis_per_migrar')#migrar codi
        dir_list.pop(0)
    print("############Sortint de " + path_act.split("/")[-1] + "############")
    
path="dataset"
funcio(path)
