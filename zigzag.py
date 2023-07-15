# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Write the code that will take a string and make this conversion given a number of rows:

# string convert(string s, int numRows);
 

# Example 1:

# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:

# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P(0,0)               I(0,3)    N
# A(1,0)        L(1,2) S(1,3)  I G
# Y(2,0) A(2,1)        H(2,3) R
# P(3,0)               I(3,3)

# Column 0 Row 1
# index = 0
# column = 0
# row = 0
# while index < s.lengh
    # While row <= numRows - 1
        # 0,0 index++
        # 1,0 index++
        # 2,0 index++
        # 3,0 index++

    # row=3, column=0
    # while (row >= 0)
        # while row >= 0 && 
        # row = row--
        # column ++,

# Example 3:

# if row number is (index+1) // 4 > 1 and ((index+1) % 4) % 2 == 1, then start reducing row by 1
# Populate columns from 0, 3, 7
# Input: s = "A", numRows = 1
# Output: "A"
 

# Constraints:

# 1 <= s.length <= 1000
# s consists of English letters (lower-case and upper-case), ',' and '.'.
# 1 <= numRows <= 1000

def convert(s: str, numRows: int) -> str:
    metrics = [ [0 for i in range(len(s))] for i in range(numRows)]
    
    column = 0
    row = 0
    index = 0
    while index < len(s):

        # Always start from row = 0 till last row
        row = 0
        while row < numRows and index < len(s):
            metrics[row][column] = s[index]
            row += 1
            index += 1
    
        # 
        # row = row - 2
        # Start filling diagonally upto row = 1
        row = (numRows - 1) - 1
        column += 1

        while row >= 1 and index < len(s):
            metrics[row][column] = s[index]
            index += 1
            row -= 1
            column += 1
            
    for row in metrics:
        for val in row:
            print(val, end=' ')
        print('')
            
     
    
convert("PAYPALISHIRING", 4)