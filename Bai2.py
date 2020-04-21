def SequentialSearch(list, key):
    n = len(list)
    
    for i in range(0,n):
        if (list[i] == key):
            return True
    return False   


def BinarySearch_UseRecursive(list, left, right, key):
    n = len(list)
    list.sort(reverse=False)
    mid = (left+right)//2
    if (right >= left):
        if (list[mid] == key ):
            return True
        elif (list[mid] > key):
            return BinarySearch_UseRecursive(list,mid+1, right, key)
        elif (list[mid] < key):
            return BinarySearch_UseRecursive(list, mid, right -1, key)
    return False

def BinarySearch_NotUseRecursive(list, left, right, key):
    while (left <= right):
        mid = (left+right)//2
        
        if (list[mid] == key):
            return True
        elif (list[mid] > key):
            left = mid + 1
        elif (list[mid] < key):
            right -= 1
    return False
def SelectionSort(list):
    for i in range(len(list)): 
      
   
        min_idx = i 
        for j in range(i+1, len(list)): 
            if list[min_idx] > list[j]: 
                min_idx = j 
                   
        list[i], list[min_idx] = list[min_idx], list[i] 

def heapify(arr, n, i): 
    largest = i # Initialize largest as root 
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    # See if left child of root exists and is 
    # greater than root 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # See if right child of root exists and is 
    # greater than root 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Change root, if needed 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # swap 
  
        # Heapify the root. 
        heapify(arr, n, largest) 
  

def heapSort(arr): 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n//2 - 1, -1, -1): 
        heapify(arr, n, i) 
  

    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # swap 
        heapify(arr, i, 0) 

def partition(arr,low,high): 
    i = ( low-1 )         # index of smaller element 
    pivot = arr[high]     # pivot 
  
    for j in range(low , high): 
  
        # If current element is smaller than the pivot 
        if   arr[j] < pivot: 
          
            # increment index of smaller element 
            i = i+1 
            arr[i],arr[j] = arr[j],arr[i] 
  
    arr[i+1],arr[high] = arr[high],arr[i+1] 
    return ( i+1 ) 
  

def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
  
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 
        L = arr[:mid] 
        R = arr[mid:] 
  
        mergeSort(L) 
        mergeSort(R) 
  
        i = j = k = 0
          
        
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def countingSort(arr, exp1): 
  
    n = len(arr) 
  
    output = [0] * (n) 
  
    count = [0] * (10) 
  
    for i in range(0, n): 
        index = (arr[i]//exp1) 
        count[ (index)%10 ] += 1
  
    for i in range(1,10): 
        count[i] += count[i-1] 
  
    i = n-1
    while i>=0: 
        index = (arr[i]//exp1) 
        output[ count[ (index)%10 ] - 1] = arr[i] 
        count[ (index)%10 ] -= 1
        i -= 1
  
    i = 0
    for i in range(0,len(arr)): 
        arr[i] = output[i] 
def radixSort(arr): 
  
    max1 = max(arr) 
  
    exp = 1
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10
list = [1,2,3,4,5,88,45,50]



print(list)
radixSort(list)
print(list)