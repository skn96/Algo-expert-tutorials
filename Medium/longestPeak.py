def longestPeak(array): 
    longest_peak_length = 0

    for i in range(1, len(array) - 1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            print(f"Found a peak at index {i} with value {array[i]}")
            lp = i-1
            rp = i+1
            print(f"Left side: {lp}, Right side: {rp}")
            left_val = 1
            right_val = 1
            while array[lp] > array[lp-1]:
                left_val += 1
                print(f"Left side: {array[lp]} > {array[lp-1]}")
                lp -= 1
                
            while array[rp] > array[rp+1]:
                print(f"Right side: {array[rp]} > {array[rp+1]}")
                right_val += 1
                rp += 1

            print(f"Left side length: {left_val}, Right side length: {right_val}\n")
            current_peak_length = left_val + right_val + 1
            longest_peak_length = max(longest_peak_length, current_peak_length)
    return longest_peak_length


test_array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]
print(f"The longest peak in the array is {longestPeak(test_array)}")