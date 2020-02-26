# public int minSteps(int[] piles){
#     int len = piles.length;
#     if(len <= 1) return 0;
#     Arrays.sort(piles);
#     int res = 0, distinctNums = 0;
#     for(int i = 1; i < len; ++i){
#         if(piles[i] == piles[i - 1]){
#             res += distinctNums;
#         }
#         else{
#             ++distinctNums;
#             res += distinctNums;
#         }
#     }
#     return res;
# }

def minSteps(piles):
    if len(piles) <= 1:
        return 0
    piles.sort()
    res = 0
    distinctNums = 0
    for i in range(1,len(piles)):
        if piles[i] == piles[i-1]:
            res += distinctNums
        else:
            distinctNums += 1
            res += distinctNums
    return res

print(minSteps([5,2,1]))