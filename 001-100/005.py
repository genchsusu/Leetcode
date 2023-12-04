'''
最长回文子串
给定一个字符串 s, 找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。

示例 2
输入: "cbbd"
输出: "bb"

https://leetcode-cn.com/problems/longest-palindromic-substring/
# Manacher算法
'''
def longestPalindrome(s: str) -> str:
    # Transform s into the format like "#a#b#c#"
    def preprocess(s: str) -> str:
        return '#' + '#'.join(s) + '#'

    t = preprocess(s)
    n = len(t)
    
    # Initialize center and right border
    center, right = 0, 0
    # Initialize palindrome span for each character as center
    p = [0] * n
    max_len = 0
    start = 0  # Starting position of the longest palindrome

    for i in range(n):
        # Mirror of i with respect to the center
        mirror = 2*center - i
        # If i is within the right border
        if right > i:
            p[i] = min(right-i, p[mirror])
        # Attempt to expand palindrome centered at i
        a, b = i + (1 + p[i]), i - (1 + p[i])
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        # Update center and right border if needed
        if i + p[i] > right:
            center, right = i, i + p[i]
        # Update longest palindrome info
        if p[i] > max_len:
            max_len = p[i]
            start = (i - max_len) // 2  # Convert back to original string index

    # Return the longest palindrome in the original string
    return s[start: start+max_len]

print(longestPalindrome("abdccba"))
print(longestPalindrome("abccba"))