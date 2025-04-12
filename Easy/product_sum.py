def productSum(array, multiplier = 1): 
    sum = 0
    for element in array: 
        if type(element) is list: 
            productSum(element, multiplier+1)
        else: 
            sum += element

    return multiplier*sum

array = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(f"Product sum: {productSum(array)}")