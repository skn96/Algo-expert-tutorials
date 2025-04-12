def firstNonRepeatingCharacter(array): 
    letters = {}
    for letter in array: 
        if letter not in letters.keys():
            letters[letter] = 0
        
        letters[letter] += 1

    for l in letters.keys():
        if letters[l] == 1:
            return l 
    
    return "_"

test_string = "abcdbcafdf"
print(f"First non repeating character: {firstNonRepeatingCharacter(test_string)}")
