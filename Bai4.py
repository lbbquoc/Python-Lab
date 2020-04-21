# file = open("Q:\Python 3\BaiTapThucHanh\Week 1\quoc.txt", encoding='utf-8')
# print(file)
# data = file.readlines()
# print(data)

# file.close()

def readFile(fileName):
    file = open(fileName, encoding='utf-8')
    data = file.read()
    print(data)

def CountWords(fileName):
    count = 0
    file = open(fileName, encoding= 'utf-8')
    data = file.readline()
    for line in data:
        for i in line:
            if (i == " "):
                count+=1
    print("Number of words in file",count + 1)

def CountKeyWord(fileName):
    d = dict()
    text = open(fileName,"r") #open file, now text contain data of file
    key = input("Enter the key word: ")
    for line in text:
        line = line.strip()
        words = line.split(" ")

        for word in words:
            if (word in d):
                d[word] = d[word] + 1
            else:
                d[word] = 1 
    if (key in d):
        print(key, " : ", d[key])
    else:
        print("Key word not exist !")

def ChangeWordInFile(fileName):
    text = open(fileName, "r")
    list = []
    count = 0
    keyWanaChange = input("Enter key word that u want to change : ")
    Change = input("what word u want to change for: ")
    for line in text :
        words = line.split(" ")
        for i in words:
            list.insert(count,i)
            count+=1
    num = len(list)
    for i in range(num):
        if (list[i].strip() == keyWanaChange):
            if ("\n" in list[i]):
                list[i]  = Change + "\n"
            else:
                list[i] = Change
    fileOut = input("Enter file location to storage: ")
    text_new = open(fileOut, "w")
    str = ""
    for i in list:
        str+=" " + i
    text_new.write(str)

#Ghi toàn bộ các từ đầu câu hoặc đầu đoạn văn vào file
def writeFileE(filename):
    #path = "Q:\Python 3\BaiTapThucHanh\Week 1\quocW.txt"
    path = input("Enter file output :")
    writeF = open(path, "a+")
    f = open (filename,"r")
    line = f.readlines()
    f.close()
    for word in line:
        word = word.split()
        writeF.write(word[0] + " ")
    writeF.close()

#Ghi toàn bộ các từ có nhiều hơn 5 kí tự vào file có đuôi ".txt"
def writeFileF(fileName):
    #path = "Q:\Python 3\BaiTapThucHanh\Week 1\quocWF.txt"
    path = input("Enter file output :")
    writeF = open(path,"a+")
    f = open(fileName,"r")
    line = f.readlines()
    f.close()
    for word in line:
        word = word.split()
        for i in word:
            if len(i) > 5 :
                writeF.write(i + " ")
    writeF.close()    
## ----------------------------------- ### test case :!
# fileName = "Q:\Python 3\BaiTapThucHanh\Week 1\quoc.txt"
# writeFileE(fileName)
# writeFileF(fileName)


# print(words)
# print(list)









