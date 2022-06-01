import pykakasi
kks = pykakasi.kakasi()
text = "阿嬢"
result = kks.convert(text)
print(result)
for item in result:
    print("{}[{}] ".format(item['orig'], item['hepburn'].capitalize()), end='')
print()