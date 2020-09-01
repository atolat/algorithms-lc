# 38. Count and Say
# Easy

# The count-and-say sequence is the sequence of integers with the first five terms as following:

# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.

# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def next_number(s):
            result = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                result.append(str(count) + s[i])
                i += 1
            return ''.join(result)

        s = '1'
        for _ in range(1, n):
            s = next_number(s)
        return s
