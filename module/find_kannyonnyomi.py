import os

with open('input.txt', 'r', encoding='UTF-8') as inputfile:
    inputls = inputfile.readlines()
    outputls = []
    allproces = len(inputls)
    n=1
    for line in inputls:
        n += 1
        print(str(n)+'/'+str(allproces))
        if '慣用読み' in line:
            outputls.append(line)
        else:
            continue
with open('output.txt', 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")
