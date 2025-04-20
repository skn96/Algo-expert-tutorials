"""
Given an array of positive integers nums and an integer k, 
find the length of the longest subarray whose sum is less than or equal to k. 
This is the problem we have been talking about above. We will now formally solve it.
"""

def findLongestSubarray(nums, k): 
    l = 0
    curr = ans = 0
    for r in range(len(nums)):
        curr += nums[r]
        while curr > k: 
            l += 1
            curr -= nums[l] 

        ans = max(ans, r - l + 1)

    return ans

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
target = 8 

print(f"The longest valid subarray is {findLongestSubarray(nums, target)}")