def longestSubs(s):
    curr = 0
    end = 1
    c = s[0]
    count = 1
    maxLen = 1
    start = 0
    
    while end < len(s):
        if s[end] == c:
            count += 1
            
            if count == 2:
                if end - curr + 1 > maxLen:
                    maxLen = end - curr + 1
                    start = curr
            else :
                curr = end - 1
                
        else:
            c = s[end]
            count = 1
            if end - curr + 1 > maxLen:
                maxLen = end - curr + 1
                start = curr
        end += 1
        
    return maxLen


s1 = "baaabbabbb";
s2 = "babba";
s3 = "abaaaa";
s4 = "a";
print(longestSubs(s1))
print(longestSubs(s2))
print(longestSubs(s3))
print(longestSubs(s4))
