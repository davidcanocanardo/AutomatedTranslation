import os
import matplotlib.pyplot as plt

total = 0
num=0
llista=list()


def plot_list(lst):
    plt.plot(lst)
    plt.show()

def inserta(x):
    global llista
    i = 0
    j = len(llista)-1
    m = int((i + j)/2)
    if(j==-1):
        llista.append(x)
    elif(j==1):
        if(x<llista[0]):
            llista.insert(0,x)
        elif(x<llista[1]):
            llista.insert(1,x)
        else:
            llista.append(x)
    else:
        if(j>1):
            while((i<j) and (x<llista[m] or x>llista[m+1])):
                if(x>llista[m]):
                    i=m+1
                else:
                    j=m-1
                m = int((i + j)/2)
        if(x<=llista[m]):
            llista.insert(m,x)
        if(x>llista[m]):
            llista.insert(m+1,x)

def funcio(path_act):
    global total, num
    
    dir_list = os.listdir(path_act)
    cont = 0
    while len(dir_list)>cont:
        act_dir = dir_list[cont]
        #-----------https://www.w3resource.com/python-exercises/python-basic-exercise-85.php---------------- cerca si és un directori
        if (os.path.isdir("./" + path_act + "/" + act_dir)):
            print("------------Entrant a  " + act_dir + "------------")
            funcio(path_act + "/" + act_dir)
        elif act_dir[-7:]=="_EA.txt":
            with open(path_act + "/" + act_dir, 'r') as file:
                    code1 = file.read()
                    total += float(code1)
                    inserta(float(code1))
                    num += 1  
        cont += 1
    

path="dataset"
funcio(path)
print("total: " + str(total))
print("num. de migracions: " + str(num))
print("mitjana: " + str(total/num))
print("mediana: " + str(llista[int(num/2)]))
plot_list(llista)

