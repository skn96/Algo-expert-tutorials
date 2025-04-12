def generate_document(test_string, target_string): 
    test_dict = {}

    for letter in test_string: 
        if letter not in test_dict:
            test_dict[letter] = 1
        else: 
            test_dict[letter] += 1

    for letter in target_string: 
        if letter not in test_dict.keys() or test_dict[letter] == 0: 
            return False
        
        test_dict[letter] -= 1

    return True


test_string =   "dabb yos i twaSga"
target_string = "Swagat is bad boy"

print(f"Is there a match: {generate_document(test_string, target_string)}")
        
