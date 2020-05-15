def longestSubStr(s):
    res  = []
    res.append(s[0])
    count = 1
    
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            count = 1
        if count < 3:
            res.append(s[i])
            
    return ''.join(res)

print(longestSubStr('eedaaad'))
print(longestSubStr('xxxtxxx'))
print(longestSubStr('uuuuxaaaaxuuu'))