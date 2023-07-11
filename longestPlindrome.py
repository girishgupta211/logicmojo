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


def checkPalindrome(s):
     if s == '':
          return False
     n = len(s)
     i = 0
     while i <= n//2:
          if s[i] != s[n-1-i]:
            return False
          i+=1
     return True
    
    
def longestPalindromeV1(s):
    size = len(s)
    max_lenght = 0
    for i in range(size):
         for j in range(i+1, size):
              print("calculating palindome for s ", i, j, s[i:j])
              is_palindrome = checkPalindrome(s[i:j])
              if is_palindrome:
                   max_lenght = max(max_lenght, j-i + 1)
    #      print(s[i])
    return max_lenght


def get_palindrome_leght(s, mid_index):
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
        length = get_palindrome_leght(s,i)
        max_lenght = max(max_lenght, length)
        # TODO even length palindrome
        
    return max_lenght

s = "acbabcf"
s = "abcdcb"
# longestPalindrome(s)
ans = longestPalindromeV1(s)
print(ans)