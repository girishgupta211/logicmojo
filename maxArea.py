# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

 

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

def maxArea(height) -> int:
    left = 0
    right = len(height) - 1
    max_water = -1
    while left < right:
        currArea = (right - left ) * min(height[left], height[right])
        max_water = max(max_water, currArea)

        if height[left] > height[right]:
            right -= 1
        else:
            left += 1

    return max_water

print(maxArea([1,8,6,2,5,4,8,3,7]))