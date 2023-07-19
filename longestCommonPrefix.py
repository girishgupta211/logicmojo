# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

# def longestCommonPrefix(strs) -> str:
#     shortest_str = float('inf')
#     for str in strs:
#         shortest_str = min(shortest_str, len(str))
#     loggestPrefixLength = 0

#     for i in range(shortest_str):
#         char = strs[0][i]
#         for str in strs:
#             if str[i] != char:
#                 return loggestPrefixLength

#         loggestPrefixLength += 1      
        
#     return loggestPrefixLength


def longestCommonPrefix(strs) -> str:
    loggestPrefix = ""

    for chars in zip(*strs):
        if len(set(chars)) == 1:
            loggestPrefix += chars[0]
        else:
            break

    return loggestPrefix

print(longestCommonPrefix(["flower","flow","flight"]))
