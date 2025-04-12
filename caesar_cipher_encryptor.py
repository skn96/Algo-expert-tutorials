def caesarCipherEncryptor(string, key): 
    key = key % 26
    my_alphabets = list("abcdefghijklmnopqrstuvwxyz")
    new_string = []
    for letter in string: 
        updated_letter = cipherCode(letter, key, my_alphabets)
        new_string.append(updated_letter)

    return "".join(new_string)

def cipherCode(letter, key, my_alphabets): 
        new_code = my_alphabets.index(letter) + key
        return my_alphabets[new_code] if new_code <= 25 else my_alphabets[-1 + new_code%25]

my_string = "abc"
print(f"Updated string: {caesarCipherEncryptor(my_string, 26)}")   
    
