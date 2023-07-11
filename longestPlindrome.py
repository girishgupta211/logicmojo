# Given a string s, return the longest 
# palindromic
 
# substring
#  in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def check_palindrone(s, mid_index):
    n = len(s)
    i = 1
    # Check all left and right
    while mid_index-i >=0 and mid_index+i <=n-1 and s[mid_index-i] == s[mid_index+i]:
            i += 1

    return 1 + 2*(i-1)

def longestPalindrome(s):
    size = len(s)
    max_lenght = 0
    for i in range(size):
        # Check odd lenght palindrome
        length = check_palindrone(s,i)
        max_lenght = max(max_lenght, length)
        # TODO even length palindrome
        
    return max_lenght

s = "acbabcf"
longestPalindrome(s)
