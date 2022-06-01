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
            CN = p.get_initials(line)
            Special = " "
            JP = ''
            if 'L' in CN:
                if 'r' in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "T"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 'r' not in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "F"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
            elif 'N' in CN:
                if 'n' in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "T"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
                elif 'n' not in item['hepburn']:
                    if len(item['orig']) != 1:
                        Special = "F"
                        JP = "{} {}".format(item['orig'], item['hepburn'])
            outputls.append(JP+' '+Special+'\n')
with open('output.txt', 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")
