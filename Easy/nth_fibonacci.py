# Three different ways to evaluate the n^{th} fibonacci number 

# (1) Recursive algorithm without memorization
# O(2^n) in time and O(N) in space

def fiboRecursive(n:int)->int:
    if n == 1:
        return 0
    elif n == 2: 
        return 1
    else:
        return fiboRecursive(n-1) + fiboRecursive(n-2)
    
# (2) Recursive algorithm with memorization 
# O(N) in space and O(N) in time 

def fiboMemorize(n):
    fibo_hash = {
        1: 0,
        2: 1
    }
    if n in fibo_hash:
        return fibo_hash[n]
    else:
        fibo_hash[n] =  fiboMemorize(n-1) + fiboMemorize(n-2)
        return fibo_hash[n]

# This is O(N) in time and O(1) in space
def fiboIterative(n):
    nums = [0, 1]
    #count = nums[0] + nums[1]
    iter = 2
    if n == 1:
        return nums[0]
    elif n == 2: 
        return nums[1]
    else:
        while iter != n: 
            iter += 1
            count = nums[0] + nums[1]
            nums[0] = nums[1]
            nums[1] = count
            print(f"iter: {iter}, fibo: {count}")
        return count

n = 10
print(f"The {n}th fibonacci number is {fiboIterative(n)}") 