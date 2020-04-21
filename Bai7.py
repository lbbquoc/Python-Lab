import numpy as np

# matrix = [[1, 4, 5, 12], 
#          [-5, 8, 9, 0],
#          [-6, 7, 11, 19]]

#print(len(matrix))
def SumRow(row):
    sum = 0
    for i in row:
        sum+=i
    return sum

def sortOnRow(matrix):
    for row in range(len(matrix)):
        if (row == len(matrix) - 1):
            return matrix
        if (SumRow(matrix[row]) > SumRow(matrix[row+1])):
            temp = matrix[row] 
            matrix[row] = matrix[row + 1]
            matrix[row + 1] = temp

def check2Matrix(matrix_1,matrix_2):
    columOfMatrix1 = len(matrix_1[0])
    columOfMatrix2 = len(matrix_2[0])
    rowOfMatrix1 = len(matrix_1)
    rowOfMatrix2 = len(matrix_2)
    option = [False,False] # dùng để coi 2 ma trận có thể nhân hay cộng
                # quy định phần tử 0 : cộng, phần tử 1 : nhân
                # true : có thể thực hiện được option
                # false : không thực hiện được option
    if (rowOfMatrix1 == rowOfMatrix2 and columOfMatrix1 == columOfMatrix2):
            print("can add 2 numbers ")
            option [0] = True
    else:
        print("cannot add 2 numbers ")
        option[0] = False
    if (columOfMatrix1 == rowOfMatrix2):
        print("can multiply 2 numbers to Matrix",rowOfMatrix1 ,"x",columOfMatrix2)
        option[1] = True
    else:
        print("cannot multiply 2 numbers to Matrix",rowOfMatrix1 ,"x",columOfMatrix2)
        option[1] = False
    return option
        
def sum_Of_2_Matrix(matrix_1,matrix_2): # xem comment dòng 28 
    option = check2Matrix(matrix_1,matrix_2)
    if (option[0] == False):
        return 
    else:
        row =  len(matrix_1)
        colum = len(matrix_1[0])
        newMatrix = np.arange(row*colum).reshape(row,colum) # tạo ra mt tự động với thư viện numpy
        for i in range(len(matrix_1)):
            for j in range(len(matrix_1[0])):
                newMatrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
        return newMatrix
        

def Mul_Of_2_Matrix(matrix_1,matrix_2): # xem comment dòng 28 
    option = check2Matrix(matrix_1,matrix_2)
    if (option[1] == False):
        return 
    else:
        row =  len(matrix_1)
        colum = len(matrix_2[0])
        newMatrix = np.arange(row*colum).reshape(row,colum) # tạo ra mt tự động với thư viện numpy
        for row in range(len(newMatrix)):
            for col in range(len(newMatrix[0])):
                newMatrix[row][col] = 0 # set lại phần tử cho mt mới này = 0 hết 
        for i in range(len(matrix_1)):
            for j in range(len(matrix_2[0])): # lấy chỉ số cột của mt 1
                for k in range(len(matrix_2)):
                    newMatrix[i][j] += matrix_1[i][k] * matrix_2[k][j]
        return newMatrix

def isMagicSquare( matrix) : 
    N = len(matrix)
    s = 0 
      
    for i in range(0, N) : 
        s = s + matrix[i][i] 
  

    s2 = 0
    for i in range(0, N) : 
        s2 = s2 + matrix[i][N-i-1] 
  
    if(s!=s2) : 
        return False
  

    for i in range(0, N) : 
        rowSum = 0;      
        for j in range(0, N) : 
            rowSum += matrix[i][j] 
          
        
        if (rowSum != s) : 
            return False
  
 
    for i in range(0, N): 
        colSum = 0
        for j in range(0, N) : 
            colSum += matrix[j][i] 
  
     
        if (s != colSum) : 
            return False
  
    return True

# # newMatrix = sortOnRow(matrix)
# # print(newMatrix)
# matrix_A = [[1, 4, 5, 12], 
#            [-5, 8, 9, 0],
#            [-6, 7, 11, 19]]
# matrix_B = [[1, 2, 5, 12], 
#            [-5, 8, 19, 0],
#            [-16, 7, 11, 9]]
# matrix_C = [[1, 4, 5], 
#            [-5, 8, 9],
#            [-6, 7, 12],
#            [7,9,-4]]
# #check2Matrix(matrix_A,matrix_B)
# # 3x3 matrix
# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
# # 3x4 matrix
# Y = [[5,8,1,2],
#     [6,7,3,0],
#     [4,5,9,1]]

# mat = [ [ 2, 7, 6 ], 
#         [ 9, 5, 1 ], 
#         [ 4, 3, 8 ] ] 

# if (isMagicSquare(mat)) : 
#     print( "Magic Square") 
# else : 
#     print( "Not a magic Square") 


