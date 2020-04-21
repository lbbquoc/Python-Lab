def FindMax(arr):
   
    max = arr[0]
    for i in arr :
        if (i > max):
            max = i
    return max

def Sum(arr):
    sum=0
    n = len(arr)
    for i in range(0,n):
        sum+=arr[i]
    return sum
def Check_Ascending(arr):
    n = len(arr)
    flag = False
    for i in range(0,n-1):
        if(arr[i] < arr[i+1]):
            flag =True
        else:
            flag =False
    if(flag == True):
        print("The array is ascending !")
    else:
        print('The array is not ascending !')

def Check_Decrease(arr):
    n = len(arr)
    flag = False
    for i in range(0,n-1):
        if(arr[i]>arr[i+1]):
            flag=True
        else:
            flag=False
    if(flag == True):
        print("the array is decrease !")
    else:
        print("the array is not decrease !")
def Count_Integer(arr):
    x = 0
    count_OOD = 0
    count_Even = 0;
    for i in arr :
        if (type(i) == type(x)):
            x+=1
            if(i %2 == 0):
                count_Even+=1
            else:
                count_OOD+=1
    print("Numbers of integer is: ",x)
    print("Numbers of Odd Integer is:",count_OOD)
    print("Number of Even Integer is:",count_Even)


        
# a = [1, 2,7,4,8,10,12.5]
# print("Max is:", FindMax(a))
# print ("Sum is :",Sum(a))
# (Check_Ascending(a))
# Check_Decrease(a)
# Count_Integer(a)