# Longest Repeating Subsequence
# Given a sequence, find the length of its longest repeating subsequence (LRS). A repeating subsequence will be the one that appears at least twice in the original sequence and is not overlapping (i.e. none of the corresponding characters in the repeating subsequences have the same index).

# Example 1:

# Input: “t o m o r r o w”
# Output: 2
# Explanation: The longest repeating subsequence is “or” {tomorrow}.

# Example 2:

# Input: “a a b d b c e c”
# Output: 3
# Explanation: The longest repeating subsequence is “a b c” {a a b d b c e c}.

# Example 3:

# Input: “f m f f”
# Output: 2
# Explanation: The longest repeating subsequence is “f f” {f m f f, f m f f}. Please note the second last character is shared in LRS.

def find_LRS_length(str):
    n = len(str)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    maxLength = 0
    # dp[i1][i2] will be storing the LRS up to str[0..i1-1][0..i2-1]
    # this also means that subsequences of length zero(first row and column of
    # dp[][]), will always have LRS of size zero.
    for i1 in range(1, n+1):
        for i2 in range(1, n+1):
            if i1 != i2 and str[i1 - 1] == str[i2 - 1]:
                dp[i1][i2] = 1 + dp[i1 - 1][i2 - 1]
            else:
                dp[i1][i2] = max(dp[i1 - 1][i2], dp[i1][i2 - 1])

            maxLength = max(maxLength, dp[i1][i2])

    return maxLength


def main():
    print(find_LRS_length("tomorrow"))
    print(find_LRS_length("aabdbcec"))
    print(find_LRS_length("fmff"))


main()
