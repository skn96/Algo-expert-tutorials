# This is a program to check if a given string is a palindrome or not

# Approach 1 : Using two pointers
# O(n) in time and O(1) in space
def checkPalindrome(array): 
    left = 0
    right = len(array) - 1 
    isPalindrome = True
    while left < right and isPalindrome:
        if array[left] == array[right]:
            left += 1
            right -= 1
        else:
            isPalindrome = False 
            break 
    return isPalindrome

# Approach 2: Using recursion
# O(n) in time and O(n) in space
def checkPalindromeRecursive(array, i = 0): 
    j = len(string) - 1 - i
    if i >= j:
        return True 
    else:
        return array[i] == array[j] and checkPalindromeRecursive(array, i+1)

string = "babcbb"
array_string = list(string)

isPalindromeResult = checkPalindromeRecursive(array_string)
print(f"The current string a palindrome? : {isPalindromeResult}")
