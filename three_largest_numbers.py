def findThreeLargestNumbers(array: list[int]) -> list[int]: 
    largest_nums = [0, 0, 0]

    for num in array:
        if num < largest_nums[2]:
            if num < largest_nums[1] and num > largest_nums[0]:
                largest_nums[0] = num
            elif num > largest_nums[1]:
                largest_nums[0] = largest_nums[1]
                largest_nums[1] = num 
        else:
            largest_nums[0] = largest_nums[1]
            largest_nums[1] = largest_nums[2]
            largest_nums[2] = num
        
        print(f"{largest_nums}")

    return largest_nums

array = [-1, 141, 12, 16, 42, -12, 18, 34, 11, 422, 12, 63, 12]
large_nums = findThreeLargestNumbers(array)

print(f"{large_nums}")

