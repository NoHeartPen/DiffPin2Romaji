import pykakasi
from xpinyin import Pinyin

p= Pinyin()


kks = pykakasi.kakasi()

with open('input.txt', 'r', encoding='UTF-8') as inputfile:
    inputls = inputfile.readlines()
    outputls = []
    allproces = len(inputls)
    n=1
    for line in inputls:
        line= line.strip("\n")
        n += 1
        print(str(n)+'/'+str(allproces))
        Japanseresult = kks.convert(line)
        for item in Japanseresult:
            CN = p.get_initials(line) # A-B-
            Special = " "
            JP = ''
            if 'D' in CN:
                if 'd' in item['hepburn']: # ahai
                    if len(item['orig']) != 1:
                        Special = "T"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 't' in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "F"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 'd' not in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = " "
                        JP = "{} {}".format(item['orig'], item['hepburn'])
            elif 'T' in CN:
                if 't' in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "T"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 'd' in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "F"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 'd' not in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = " "
                        JP = "{} {}".format(item['orig'], item['hepburn'])
            outputls.append(JP+' '+Special+'\n')
with open('output.txt', 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")
