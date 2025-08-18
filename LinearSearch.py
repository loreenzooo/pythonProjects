def LinearSearch(myArr, targetValue):
    for index, value in enumerate(myArr):
        if value == targetValue:
            return index
    return -1


myArr  = [5, 3, 8, 7]
targetValue = 7

result = LinearSearch(myArr, targetValue)

if result != -1:
    print(f"Found at index: {result}")
else:
    print("Not Found!")


        
    
    
