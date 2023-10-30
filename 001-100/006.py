'''
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

	P   A   H   N
	A P L S I I G
	Y   I   R

	And then read line by line: "PAHNAPLSIIGYIR"
Z 字形变换
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。之后，你的输出需要从左往右逐行读取，产生出一个新的字符串

示例1
输入: s = "LEETCODEISHIRING", numRows = 3
输出: "LCIRETOESIIGEDHN"

示例2
输入: s = "LEETCODEISHIRING", numRows = 4
输出: "LDREOEIIECIHNTSG"<br>
解释:
  L     D     R
  E   O E   I I
  E C   I H   N
  T     S     G
https://leetcode-cn.com/problems/zigzag-conversion/
'''

def zConverter(s, numRows):
    if numRows == 1:
        return s
    rows = [''] * numRows
    curRow = 0
    goingDown = False
    for c in s:
        rows[curRow] += c
        if curRow == 0 or curRow == numRows - 1:
            goingDown = not goingDown
        curRow += 1 if goingDown else -1
    return ''.join(rows)

print(zConverter("LEETCODEISHIRING", 3))
print(zConverter("LEETCODEISHIRING", 4))