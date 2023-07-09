# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

def twoSum(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]




def twoSumV2(arr, target):
    start = 0
    end = len(arr) - 1
    # Start 2 indices. one from beginning and one from last
    # if sum is equal then return 
    # If sum is less then increase initial index
    # if sum is more then decrese last index
    while start < end:
        if arr[start] + arr[end] == target:
            return [start, end]
        elif arr[start] + arr[end] < target:
            start += 1
        else:
            end -=1

def twoSumV3(arr, target):
    start = 0
    end = len(arr) - 1
    hash = {}
    # for i in range(len(arr)):
    #     hash[arr[i]] = i

    while start <= end:
        if target - arr[start] in hash:
            return start, hash[target - arr[start]]
        else:
            hash[arr[start]] = start
            start += 1

arr = [2, 7, 11, 15, 17]
target = 24
print(twoSum(arr, target))
print(twoSumV2(arr, target))
print(twoSumV3(arr, target))
