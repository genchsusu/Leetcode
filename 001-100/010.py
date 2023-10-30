'''
正则表达式匹配
给你一个字符串s和一个字符串类型匹配模式p,请你来实现一个支持'.'和'*'的正则表达式匹配。

'.' 匹配任意单个字符
'*' 匹配零个或多个前面的那一个元素
所谓匹配,是要涵盖 整个 字符串s的,而不是部分字符串 说明:

s 可能为空,且只包含从 a-z 的小写字母。
p 可能为空,且只包含从 a-z 的小写字母,以及字符 . 和 *。

示例1
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。

示例 2
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此,字符串 "aa" 可被视为 'a' 重复了一次。

示例 3
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符('.')

示例 4
输入:
s = "aab"
p = "c*a*b"
输出: true
解释: 因为 '*' 表示零个或多个,这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。

示例 5
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false

https://leetcode-cn.com/problems/regular-expression-matching/

#解题思路:动态规划
首先解题要先理解正则表达式具体匹配规则,先来做个最简单的假设:

假设s=ab,p=a*b*,那么毫无疑问s.match(p)是成立的

根据上面的例子,p变成a*b*c,那么这就是不成立的,因为s并没有c,如果p再加一个*变成a*b*c*,那么匹配又会变成立,因为c这个时候可以匹配为0个

那么当匹配到*号的时候具体到代码上逻辑是这样的:

if(p.charAt(i) === '*'){
  dp[i+1] = dp[i-1]
}
以上的逻辑思路就是当匹配到a*b*c*中时,判断最后一个*是否匹配成立只需要看第2个*,即a*b*是否匹配,如果匹配那么a*b*c*也是成立的,假如s换成是ad,那么走到a*b的时候就已经不匹配了,经过状态转移a*b*c*也不会匹配,所以使用 动态规划 就再合适不过
'''

def isMatch(s, p):
    m = len(s)
    n = len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True
    for i in range(2, n + 1):
        dp[0][i] = dp[0][i - 2] and p[i - 1] == '*'
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else:
                    dp[i][j] = dp[i][j - 2]
            else:
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[m][n]


print(isMatch("aa", "a"))
print(isMatch("aa", "a*"))
print(isMatch("baa", "a*"))
print(isMatch("ab", ".*"))