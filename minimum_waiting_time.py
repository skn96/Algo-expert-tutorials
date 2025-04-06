# Runs in O(1) Space complexity
def minimumWaitingTime(array: list[int]) -> int: 
    array.sort() # O(Nlog(N)) time complexity
    currentWaitingTime = 0
    for idx in range(0, len(array)-1):
        delayTime = array[idx]
        remainingNums = len(array) - idx - 1
        # print(f"Remaining nums: {remainingNums}")
        # print(f"The current waiting time: {currentWaitingTime}")
        currentWaitingTime += remainingNums*delayTime
        # print(f"Remaining nums: {array[idx:len(array)-1]}")
    return currentWaitingTime

array = [3,2,1,2,6] # => [1, 2, 2, 3, 6]
print(f"The current waiting time is {minimumWaitingTime(array)}\n")
