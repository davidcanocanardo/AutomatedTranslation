import re
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import os
                
def remove_comments(code):
    # Remove single-line comments starting with '//'
    code = re.sub(r'//.*', '', code)
    # Remove multi-line comments enclosed in '/* */'
    code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    return code

def compare_code(code1, code2):
    code1 = remove_comments(code1)
    code2 = remove_comments(code2)

    reference = code1.split()
    candidate = code2.split()

    smoothing_function = SmoothingFunction().method1  # Choose the smoothing method you prefer
    bleu_score = sentence_bleu([reference], candidate, smoothing_function=smoothing_function)

    return bleu_score * 100
    
def funcio(path_act):
    dir_list = os.listdir(path_act)
    cont = 0
    while len(dir_list)>cont:
        act_dir = dir_list[cont]
        #-----------https://www.w3resource.com/python-exercises/python-basic-exercise-85.php---------------- cerca si és un directori
        if (os.path.isdir("./" + path_act + "/" + act_dir)):
            print("------------Entrant a  " + act_dir + "------------")
            funcio(path_act + "/" + act_dir)
        elif (act_dir[-7:]=="_LLM.kt"):
            nom = act_dir[0:-7]
            with open(path_act +"/"+nom+".kt", 'r') as file:
                code1 = file.read()
            with open(path_act +"/"+nom+"_LLM.kt", 'r') as file:
                code2 = file.read()
            percentage = compare_code(code1, code2)
            with open(path_act +"/"+nom+"_LLM.txt", 'w') as file:
                file.write(f"{percentage}")
        cont += 1
    
path="dataset"
funcio(path)

