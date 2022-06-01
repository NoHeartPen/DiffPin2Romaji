import pykakasi


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
        JP = ''
        Japanseresult = kks.convert(line)
        for item in Japanseresult:
            print(item)
            if len(item['orig']) != 1: # 找不到时会尝试自己拼出
                JP = item['orig']+'['+item['hepburn']+']'+' '
        outputls.append(JP+'\n')
with open('output.txt', 'w', encoding='UTF-8') as outputfile:
    outputfile.writelines(outputls)
print("Done")
