"""
You are given a binary string s (a string containing only "0" and "1"). 
You may choose up to one "0" and flip it to a "1". 
What is the length of the longest substring achievable that contains only "1"?
For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, 
the string becomes 1111100111.
"""

def findLongestSubstring(s): 
    curr = l = ans = 0
    for r in range(len(s)): 
        if s[r] == "0":
            curr += 1
        while curr > 1: 
            if s[l] == "0":
                curr -= 1
            l += 1

        ans = max(ans, r - l + 1)
    return ans

my_string = "1101100111"
print(f"The length of the longest substring is {findLongestSubstring(my_string)}")
