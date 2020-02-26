def longestStr(s):
    if not s:
        return ""
    if len(s) == 1:
        return ""
    n = len(s)
    for i in range(1,n):
        if s[i-1] > s[i]:
            return s[:i-1] + s[i:]
        
    return s[:-1]


print(longestStr('abczd'))
print(longestStr('abcd'))