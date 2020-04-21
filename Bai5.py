#file_name = "Q:\Python 3\BaiTapThucHanh\Week 1\contacts.txt"


def readData(file_name):
    data = open(file_name, "r")
    for text in data:
        print(text)

def sortByName(file_name):
    name = ""
    list=[]
    data = open(file_name, "r")
    for text in data:
        for i in text:
            if(i != ","):
                name += i
            else:
                list.insert(0,name)
                name =""
                break
    list.sort()
    for i in list:
        print(i)
def checkInfo(file_name):
    key = input("Enter Name: ")
    data = open(file_name, "r")
    text = data.readlines()
    for i in text:
        if i.rfind(key) != -1:
            return i
    print("Not exist !")

def editInfo(file_name):
    contact = checkInfo(file_name)
    print ("Do you wanna change Name(1) or Phone(2) :")
    option = input("choose the option:")
    if (option == "2"):
        key = input("add new number of telephone: ")
        contact = contact.split(",")[0]
        contact = contact + ", " + key 
        print( "new contact is :",contact)
        return 
    else:
        key = input("add new name: ")
        contact = contact.split(",")[1]
       # print(type(contact), contact)
        key = key + "," + contact
        print( "new contact is :",key)
        return


# string ="Quoc, 555-1234"
# print(string.split(","))
# print(string)
# string = string.split(",")[:-1]
# print(string)

sortByName(file_name)