def runLengthEncoding(string):
    # AAAAAAAAAAAAABBCCCCDD -> 9A2B4C2D
    # Constraints: Has atleast one character
    my_array = list(string)
    length = 1
    encoded_list = []

    for idx in range(1, len(my_array)):
        if my_array[idx] == my_array[idx-1] and idx != 9:
            length += 1
        else:
            encoded_list.append(str(length))
            encoded_list.append(my_array[idx-1])
            length = 1

    encoded_list.append(str(length))
    encoded_list.append(my_array[idx-1])
    return "".join(encoded_list)

my_string = "AAAAAAAAAAAAABBCCCCDD"
print(f"Encoded string is: {runLengthEncoding(my_string)}")