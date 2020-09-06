# 774. Minimize Max Distance to Gas Station
# Hard

# On a horizontal number line, we have gas stations at positions stations[0], stations[1], ..., stations[N-1],
# where N = stations.length.

# Now, we add K more gas stations so that D, the maximum distance between adjacent gas stations, is minimized.

# Return the smallest possible value of D.

# Example:

# Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K = 9
# Output: 0.500000

class Solution(object):
    def minmaxGasDist(self, stations, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        # Use bisection search to optimize distance between gas stations
        start = 0
        end = 0
        # The end of the range is the max distance between two adj stations
        for i in range(len(stations)-1):
            end = max(end, stations[i+1]-stations[i])

        while start <= end - 0.000001:
            mid = (start+end)/2.0
            # Given the value of mid,
            # figure out how many gas stations are needed to achieve it
            num = 0
            for i in range(len(stations) - 1):
                num += math.floor((stations[i+1]-stations[i])/mid)
            # More the stations, lesser the distance
            # Smaller values of D are not achievable with K stations
            # Increase D, move right!
            if num > K:
                start = mid
            else:
                end = mid

        return start
