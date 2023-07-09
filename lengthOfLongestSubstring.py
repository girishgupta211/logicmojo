# Given a string s, find the length of the longest substring without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# # s consists of English letters, digits, symbols and spaces.

# def lengthOfLongestSubstring(str):
#     print(str)
#     # Create an bitmap of 128 chars
#     # Will store the ascii value of these characters
#     # begin from start to end
#     # keep track of start and end of substring.
#     # If There is any duplicate value, then reset start. and keep lenght of substr as maximum
#     bitMap = [0]*128
#     start_index = 0
#     end_index = 0
#     max_lenght = 0
#     # print(bitMap)
#     for index in range(len(s)):
#         # print(index, s[index])
#         # print(ord(s[index]))
#         if bitMap[ord(s[index])] == 1:
#             # print(bitMap)
#             bitMap = [0]*128
#             bitMap[ord(s[index])] == 1
#             substr_lenght = end_index - start_index + 1
#             max_lenght = max(max_lenght, substr_lenght)
#             print(str[start_index:end_index+1])
#             start_index = index
#             end_index = index
#         else:
#             bitMap[ord(s[index])] += 1
#             end_index = index
#     return max_lenght

# def longestSubstringWithoutRepeatingCharactersV2(string):
#   freq_arr = [0]*128 
#   left_index = 0
#   max_length = 0
#   right_index = 0
#   while right_index < len(string):
#     freq_arr[ord(string[right_index])] += 1
    
#     # If frequey of any string is more than 1, 
#     # Then discard all elements left of this element and decrease frequency of left
#     while freq_arr[ord(string[right_index])] > 1:
#       freq_arr[ord(string[left_index])] -= 1
#       left_index += 1
#     max_length = max(max_length, right_index-left_index+1)

#     right_index += 1
  
#   return max_length


def longestSubstringWithoutRepeatingCharactersV2(s):
    # This array will be used to keep track of the frequency of each character encountered in the string.
    frequency_arr = [0]*128

    # keep track of the starting index of the current substring
    left_index = 0

    right_index = 0

    #  store the maximum length found so far of substring
    max_lenght = 0
    while right_index < len(s):
        element = s[right_index]
        # print(element)

        # . The ord() function converts the character to its corresponding ASCII value, which is used as the index in the freq_arr array.
        frequency_arr[ord(element)] +=1
        # print(frequency_arr)

        # After updating the frequency array, the code enters another while loop if the frequency of the current character is greater than 1. 
        # This means that the current character is repeating in the substring.

        while frequency_arr[ord(element)] > 1:
            # discard all elements to the left of the repeating character and adjust the substring accordingly.
            frequency_arr[ord(s[left_index])] -= 1
            left_index += 1

        max_lenght = max(max_lenght, right_index-left_index + 1)
        # print(max_lenght)
        right_index += 1
    
    return max_lenght
# s = "abcabcbbac"    
s = 'geeksforgeeks'
ans = longestSubstringWithoutRepeatingCharactersV2(s)
print(ans)
s = 'geeksforgeeks'
