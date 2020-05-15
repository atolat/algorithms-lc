# public int MaximumPossibleValue(int N) {
#         // write your code here
#         StringBuilder sb = new StringBuilder(String.valueOf(Math.abs(N)));
#         int flag = N >= 0 ? 1 : -1;
#         if (N >= 0) {
#             int idx = 0;
#             while (idx < sb.length() && (sb.charAt(idx) - '0') >= 5) {
#                 idx++;
#             }
#             sb.insert(idx, 5);
#         } else {
#             int idx = 0;
#             while (idx < sb.length() && (sb.charAt(idx) - '0') <= 5)
#                 idx++;
#             sb.insert(idx, 5);
#         }
#         int val = Integer.parseInt(sb.toString());
#         return flag * val;
#     }

def maxPossibleVal(N):
    result = list(str(N))
    # flag = True
    # if N < 0:
    #     flag = False
        
    if N >= 0:
        idx = 0
        while idx < len(result) and int(result[idx]) - 0 >= 5:
            idx += 1
        result.insert(idx, '5')
    
    else:
        idx = 1
        while idx < len(result) and int(result[idx]) - 0 <= 5:
            idx += 1
        result.insert(idx, '5')
        
    value = int(''.join(result))
    # if flag == False:
    #     return value
    # else:
    return value

def make_maximum(val):
    def helper(lst, pos):
        if pos == 0:
            return int(''.join(['5']+ lst))
        elif pos < len(lst):
            return int(''.join(lst[:pos] + ['5'] + lst[pos:]))
        else:
            return int(''.join(lst + ['5']))


    if val < 0: 
        digits = [i for i in str(val)[1:]]
    else:
        digits = [i for i in str(val)]


    nums = []
    for pos in range(0, len(digits)+1):
        nums.append(helper(digits, pos))
    if val>=0:
        return max(nums)
    else:
        return -1 * min(nums)

print(maxPossibleVal(268))
print(maxPossibleVal(670))
print(maxPossibleVal(0))
print(maxPossibleVal(-999))

print(make_maximum(268))
print(make_maximum(670))
print(make_maximum(0))
print(make_maximum(-999))