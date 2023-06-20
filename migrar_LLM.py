import os
import clipboard
                

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
            if (dir_list.count(act_dir[0:-5] + "_LLM.kt")==0):
                print("\n\n\nCan you translate this code from Java to Kotlin? Do not print empty lines")
                with open(path_act +"/"+act_dir, 'r') as file:
                    code = file.read()
                    code = code.splitlines()
                    code = [line for line in code if line.strip()]
                    code = '\n'.join(code)
                    print(code)
                    #clipboard.copy(code)
                print("\n\n\nEntra la resposta:")
                
                lines = []
                while True:
                    line = input()
                    if line:
                        lines.append(line)
                    else:
                        break
                resposta = '\n'.join(lines)
                with open(path_act +"/"+act_dir[0:-5]+"_LLM.kt", 'w+') as file:
                    file.write(f"{resposta}")
                    print("#########Escrivint a " +path_act +"/"+act_dir[0:-5]+"_LLM.kt")
                    file.close()
        cont += 1
    
path="dataset"
funcio(path)

