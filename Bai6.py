import math
import random

class   Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        

def CalDistance(x1,y1,x2,y2):
    diemA = Point2D(x1,y1)
    diemB = Point2D(x2,y2)
    return round(math.sqrt(pow(diemB.x - diemA.x,2) + pow(diemB.y - diemA.y, 2)),2)
# round dùng để làm tròn cú pháp : round(<số>, <làm tròn đến chữ số hàng ?> )

def createTriangle(x1,y1,x2,y2,x3,y3):
    AB = CalDistance(x1,y1,x2,y2)
    AC = CalDistance(x1,y1,x3,y3)
    BC = CalDistance(x2,y2,x3,y3)    
    print(AB,AC,BC)
    if (AB + BC > AC or AB + AC > BC or BC + AC >AB ):
        return True
    else:
        return False

def calCircumference(a,b,c):
    return a+b+c
def calArea(a,b,c):
    p = calCircumference(a,b,c) / 2
    return math.sqrt(p*(p-a)*(p-b)*(p-c)) 
def whatIsTriangle(x1,y1,x2,y2,x3,y3):
    if createTriangle(x1,y1,x2,y2,x3,y3):
        AB = CalDistance(x1,y1,x2,y2)
        AC = CalDistance(x1,y1,x3,y3)
        BC = CalDistance(x2,y2,x3,y3)  
        if (AB == AC == BC):
            print("It is equilateral triangle\n")
            print("Circumference is : ",calCircumference(AB,BC,AC))
            print("Area is:", calArea(AB,BC,AC))
            return
        if ((AB == AC and AB != BC) or (AB == BC and AB != AC) or (BC == AC and BC != AB)):
            print("It is isosceles triangle\n")
            print("Circumference is : ",calCircumference(AB,BC,AC))
            print("Area is:", calArea(AB,BC,AC))
            return
        if (AB**2 + BC**2 == AC**2) or (AB**2 + AC**2 == BC**2) or (BC**2 + AC**2 == AB**2):
            print("It is right triangle\n")
            print("Circumference is : ",calCircumference(AB,BC,AC))
            print("Area is:", calArea(AB,BC,AC))
            return
        else: 
            print("It's normal triangle !")
            print("Circumference is : ",calCircumference(AB,BC,AC))
            print("Area is:", calArea(AB,BC,AC))
            return
    else:
        return


def GiaiPhuongTrinh2An(x1,y1,x2,y2):
    # phương trinh y = Ax + B
    list = []   
    D = x1*1 - 1*x2
    Dx = y1*1 - 1*y2
    Dy = x1*y2 - y1*x2
    print(D,Dx,Dy)
    print()
    if (D == 0 and Dx == 0):
        print("He phuong trinh vo so nghiem !")
        return
    if (D == 0 and Dx != 0):
        print("He phuong trinh vo nghiem !")
        return
    if (D != 0):
        print("Phuong trinh co nghiem: ")
        n1 = Dx / D
        n2 = Dy / D 
        print(n1,n2)
        list.insert(0,n1)
        list.insert(0,n2)
        list.reverse()
        return list


#list = GiaiPhuongTrinh2An(1,2,4,8)


def vtTuongDoiCua2DT(x1,y1,x2,y2,x3,y3,x4,y4):
    listAB = GiaiPhuongTrinh2An(x1,y1,x2,y2)
    listCD = GiaiPhuongTrinh2An(x3,y3,x4,y4)
    if((listCD[0]/listAB[0] == -1/-1) and (listCD[1]/listAB[1] == -1/-1) ):
        print("AB trung CD")    
    if (listCD[0]/listAB[0] == -1/-1) and (listCD[1]/listAB[1] != -1/-1) :
        print("AB // CD")
    if  listCD[0]/listAB[0] != -1/-1 :
        print("AB cat CD")

# lý do b2/b1 luôn bằng -1/-1 là do : mình dùng phương trình y = ax +b (mình chuyển vế y về bên tay phải sẽ có được b luôn bằng -1)


# x1 = round(random.randint(1,100),0)
# x2 = random.randint(1,100)
# x3 = random.randint(1,100)
# y1 = random.randint(1,100)
# y2 = random.randint(1,100)
# y3 = random.randint(1,100)
# x4 = random.randint(1,100)
# y4 = random.randint(1,100)
# print(x1)
# print(createTriangle(x1,y1,x2,y2,x3,y3))
# whatIsTriangle(x1,y1,x2,y2,x3,y3)
# vtTuongDoiCua2DT(x1,y1,x2,y2,x3,y3,x4,y4)



        