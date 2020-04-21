def checkPassWord(password):
    if len(password) >= 9 and len(password) <= 20:
        for i in password :
            if (i.isupper() == True):
                break
        for i in password:
            if((i.isdigit() == True)):
                break
        for i in password:
            if(i.islower() == False and i.isnumeric() == False and i.isupper() == False):
                return "PassWord is strong !"
        return "PassWord is not strong !"
        
                

def encryptPassWord(password, k):
    code =""
    for i in password:
        x = ord(i)
        y = (x+k) % 126
        if (y < 32 ):
            y+=31
        c = chr(y)
        code+=c
    return code


def decryptPassWord(password_E, k):
    code =""
    for i in password_E:
        c = i
        y = ord(c)
        x = (y - k) % 126
        if (x < 31):
            x += 95
        p = chr(x)
        code+=p
        
    return code




passW = "Mrquocno1zx123!!@@@"
# print(len(passW))
passWE = encryptPassWord(passW,10)
# for i in passWE:
#     print(ord(i))
#print(len(passWE))
decryptPassWord(passWE,10)
