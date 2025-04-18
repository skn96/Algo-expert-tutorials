def arrayOfProducts(array): 
    left_mult = [1 for _ in range(len(array))]
    right_mult = [1 for _ in range(len(array))]
    current_product = 1
    for i in range(len(array)):
        left_mult[i] = current_product
        current_product = current_product*array[i]

    print(f"Left Mult: {left_mult}")

    current_product = 1    
    for i in reversed(range(len(array))):
        right_mult[i] = current_product
        current_product = current_product*array[i]

    print(f"Right Mult: {right_mult}")

    product_array = [left_mult[i]*right_mult[i] for i in range(len(array))]
    print(f"Product Array: {product_array}")
    return product_array


# [5, 1, 4, 2]
my_product = arrayOfProducts([5, 1, 4, 2])
