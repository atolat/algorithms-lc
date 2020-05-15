# // https://leetcode.com/discuss/interview-question/398031/

# // Time Complexity: O(n)
# // Space Complexity: O(1)

# class Solution {
#     longestSubStr(s) {
#         if (s === null) {
#             return "";
#         }
#         if (s.length < 3) {
#             return s;
#         }
        
#         let curr = 0,  // current starting pointer for current substring
#             end = 1,   // the look-ahead pointer that's at the end of substring
#             c = s[0],  // current character/letter
#             count = 1, // counter for same letter consecutive appearance
#             maxlen = 1,
#             start = 0; // anchor pointer for the result's starting index
        
#         while (end < s.length) {
#             if (s[end] === c) {
#                 count++; // saw the same letter again
                
#                 // valid enough to consider to be a part of the substring
#                 if (count === 2) { 
                    
#                     // length of the current substring is greater than maxlen
#                     if (end - curr + 1 > maxlen) {
#                         maxlen = end - curr + 1; // the "+1" is to include the full substring length
#                         start = curr;            // override to be the current maxlen's start index
#                     }
#                 }
#                 else {
#                     curr = end - 1; // count > 2, therefore we need to start a new substring; reset curr
#                 }
#             }
#             else {
#                 c = s[end] // diff char/letter found; reset current char
#                 count = 1; // reset same letter consecutive appearance counter
                
#                 // length of the current substring is greater than maxlen
#                 if (end - curr + 1 > maxlen) {
#                     maxlen = end - curr + 1;
#                     start = curr;
#                 }
#             }
#             end++;
#         }
#         return s.substring(start, start + maxlen);
#     }
# }

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
        
    return s[start:start+maxLen]

print(longestSubs('aabbaaaaabb'))
print(longestSubs('aabbaabbaabbaa'))
print(longestSubs('abbaabbaaabbaaa'))