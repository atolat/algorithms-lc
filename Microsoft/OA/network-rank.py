# public class NetworkRank {

#   public static int solution(int[] A, int[] B, int N) {
#     int maxRank = 0;
#     int edgesLen = A.length;

#     int[] edgesCount = new int[N + 1];

#     for(int i=0; i<edgesLen; i++){
#       edgesCount[A[i]] += 1;
#       edgesCount[B[i]] += 1;
#     }

#     for(int i=0; i<edgesLen; i++){
#       int localMax = edgesCount[A[i]] + edgesCount[B[i]] - 1;
#       maxRank = Math.max(maxRank, localMax);
#     }

#     return maxRank;
#   }
  
def networkRank(A,B,N):
    maxRank = 0
    edgesLen = len(A)
    
    edgesCount = [0 for i in range(N+1)]
    for i in range(edgesLen):
        edgesCount[A[i]] += 1
        edgesCount[B[i]] += 1
    for i in range(edgesLen):
        localMax = edgesCount[A[i]] + edgesCount[B[i]] - 1
        maxRank = max(maxRank, localMax)
        
    return maxRank
          
    