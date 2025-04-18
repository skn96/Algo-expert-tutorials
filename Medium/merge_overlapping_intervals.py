def mergeOverlappingIntervals(array): 
    # [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
    if array:
        sorted_array = sorted(array, key= lambda x: x[0])
    else:  
        return array
    
    merged_interval = []
    current_interval = sorted_array[0]
    merged_interval.append(current_interval)

    for next_interval in sorted_array: 
        _, currentEnd = current_interval
        nextStart, nextEnd = next_interval

        if currentEnd >= nextStart:
            current_interval[1] = max(nextEnd, currentEnd)
        else: 
            current_interval = next_interval
            merged_interval.append(current_interval)

    return merged_interval

# Test cases
test_array = [[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]]
print(f"The merged intervals are {mergeOverlappingIntervals(test_array)}")

    

    

    

    