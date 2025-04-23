def singleCycleCheck(nums:list[int])->bool: 
    currentIdx = 0 
    numElementsVisited = 0

    while numElementsVisited < len(nums): 
        if numElementsVisited > 0 and currentIdx == 0: 
            return False 
        numElementsVisited += 1
        currentIdx = getNextIdx(nums, currentIdx)

        print(f"Current id: {currentIdx}, Number of elements visited: {numElementsVisited}")
        print(f"The element being considered next: {nums[currentIdx]}")

    return currentIdx == 0  
    
def getNextIdx(nums, currentIdx): 
    if currentIdx + nums[currentIdx] > len(nums) - 1: 
        return currentIdx + nums[currentIdx] - len(nums)
    elif currentIdx + nums[currentIdx] < 0:
        return currentIdx + nums[currentIdx] + len(nums)
    else:
        return currentIdx + nums[currentIdx] 
    
nums = [2, 3, 1, -4, -4, 2]
print(f"The current algorithm has a single cycle? : {singleCycleCheck(nums)}")


        

