# Alternate Min-Max Rearrangement
# 
# 
# Last Updated: May 2025
# 
# Medium
# ID 10395
# 
# 
# Question
# 
# Modify a given array of integers so that the first element is the smallest, the second is the largest, the third is the second-smallest, the fourth is the second-largest, and so on.
# 
# Constraints
# The input variable arr is a list of integers.
# The length of arr can be any non-negative integer.
# The elements in arr can be positive, negative, or zero.
# There are no specific constraints on the range of values for the elements in arr.
# 
# 
# Solution

def modify_array(arr):
    """ 
    :type arr: List[int]
    :rtype: List[int]
    """
    inc = sorted(arr)
    dec = sorted(arr, reverse=True)
    output = []
    i = 0
    
    while i < len(arr) // 2:
        output.append(inc[i])
        output.append(inc[-i-1])
        i += 1
        
    return output
