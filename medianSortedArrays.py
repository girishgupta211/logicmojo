# 4. Median of Two Sorted Arrays
# Description

# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

# 1. Briute Force approach: Merge 2 sorted arrays in O(n), then find median by taking mid element(s), then average of it.
# 2. Without merging, take mid elements of each array. say m1, m2

# array1 = [100, 200, 300, 400, 500]
# array2 = [5, 15, 25, 35, 45]

# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50] -> 27.5
# If m1(30) > m2(25), then consider left of array1 and rigth of array2
# array1 = [10, 20, 30]
# array2 = [25, 35, 45]
# If m1(20) < m2(35), then consider right of array1 and left of array2
# array1 = [20, 30]
# array2 = [25, 35]
# If number of elements are <= 2 from in both arrays then take 

# Compare m1 < m2, then take second element of array1 and first element of array2, then take average
# [1, 2]
# [3, 4]

# [1, 2]
# [3]
# 

def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return (arr[n//2])
    else:
        return (arr[n//2 - 1] + arr[n//2]) / 2
        
def medianSortedArray(arr1, arr2):
    if len(arr1) == 1 and len(arr2) == 1:
        return (arr1[0] + arr2[0]) / 2
    
    if len(arr1) == 2 and len(arr2) == 2:
        if arr1[0] < arr2[0]:
            return (arr1[1] + arr2[0])/2
        else:
            return (arr1[0] + arr2[1])/2
        
    # if len(arr1) == 1 and len(arr2) == 2:
    #     if arr2[0] > arr1[1]:
    #         return arr2[0]
        


    m1 = median(arr1)
    n1 = len(arr1)
    m2 = median(arr2)
    n2 = len(arr2)
    # If number of elements are odd, then take arr[:mid+1] for initial elements else take arr[:mid]
    # Alway take arr[mid:] for second half

    if m1 > m2:
        if n2 % 2 == 1:
            return medianSortedArray(arr2[n2//2 + 1:] , arr1[:n1//2])
        else:
            return medianSortedArray(arr2[n2//2:] , arr1[:n1//2])
    else:
        if n1 % 2 == 1:
            return medianSortedArray(arr1[n1//2 + 1:] , arr2[:n2//2])
        else:
            return medianSortedArray(arr1[n1//2:] , arr2[:n2//2])
    


# nums1 = [1, 2]
# nums2 = [3, 4]

# median = medianSortedArray(nums1, nums2)
# print('median', median)


nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 6, 8]
result = medianSortedArray(nums1, nums2)
print('result', result)


nums1 = [1, 2, 3]
nums2 = [2, 3, 6]
result = medianSortedArray(nums1, nums2)
print('result', result)

# arr = [1, 2, 3, 4]
# # first 2
# # elements
# # mid = 4/2 = 2
# # :2 -> 1, 2
# # 2: -> 3, 4


# arr = [1, 2, 3]
# # first 2
# # elements
# # mid = 3/2 = 1
# # :1 -> 1, 2
# # 2-1: -> 1: -> 3, 4
