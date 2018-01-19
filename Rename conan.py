import os

directoryname = "/media/subtleseeker/New Volume/TV Series/detective conan/130+(sub)/"

listFiles = os.listdir(directoryname)
print(listFiles)
for i in listFiles:
    os.rename(os.path.join(directoryname, i), os.path.join(directoryname, i.partition(' -')[0]))

listFiles = os.listdir(directoryname)
print(listFiles)

'''
#The other way
for i in listFiles:
    s=os.path.join(directoryname, i)
    strg = s[:(s.find("-") - 1)]
    # print(strg)
    os.rename(os.path.join(directoryname, i), os.path.join(directoryname, strg))
'''
