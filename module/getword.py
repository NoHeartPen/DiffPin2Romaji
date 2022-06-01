import os
import re


path = os.getcwd()

with open('input.txt','r', encoding='UTF-8') as inputfile:
    inputls = inputfile.readlines()
    outputls = []
    for line in inputls:
        if '【' in line:
            continue
        else:
            if re.search(r'^\w{2}$', line) != None:
                outputls.append(line)
            else:
                continue
with open('output.txt', 'w',encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")