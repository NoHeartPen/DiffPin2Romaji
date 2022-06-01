from xpinyin import Pinyin

p= Pinyin()

with open('input.txt', 'r', encoding='UTF-8') as inputfile:
    inputls = inputfile.readlines()
    outputls = []
    allproces = len(inputls)
    n=1
    for line in inputls:
        n += 1
        print(str(n)+'/'+str(allproces))
        CNoutputline = p.get_initials(line)
        outputls.append(line+CNoutputline)
with open('output.txt', 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")
