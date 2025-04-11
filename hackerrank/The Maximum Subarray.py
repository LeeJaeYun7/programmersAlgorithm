def getMaxSubarray(arr):
    maxSum = arr[0]
    currSum = arr[0]

    for i in range(1, len(arr)):
        currSum += arr[i]

        if currSum < arr[i]:
            currSum = arr[i]

        maxSum = max(maxSum, currSum)

    return maxSum


def getMaxSubSequence(arr):
    
    allMinus = True 
    
    for i in range(len(arr)):
        if arr[i] >= 0:
            allMinus = False 
            
    if allMinus == True: 
        return max(arr) 
    
    maxSubSequence = 0
    
    for i in range(len(arr)):
        if arr[i] >= 0:
            maxSubSequence += arr[i]

    return maxSubSequence

def maxSubarray(arr):
    
    a = getMaxSubarray(arr) 
    b = getMaxSubSequence(arr) 
    
    return [a,b]
