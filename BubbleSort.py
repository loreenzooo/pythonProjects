myArr = [5, 6, 3, 7, 2]
n = len(myArr)

for i in range(n-1):
    for j in range(n-1-i):
        if myArr[j] > myArr[j+1]:
            myArr[j], myArr[j+1] = myArr[j+1], myArr[j]
            
print("Sorted Array:", myArr)
        
    