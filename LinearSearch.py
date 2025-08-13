def LinearSearch(myArr, targetValue):
    for value in myArr:
        if value == targetValue:
            return 1
    return -1


myArr  = [5, 3, 8, 7]
targetValue = 3
n = myArr

result = LinearSearch(myArr, targetValue)

if result != 1:
    print("Not Found!")
else:
    print("Found")


        
    
    
