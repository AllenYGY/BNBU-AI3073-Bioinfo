def global_alignment():
    B = "GATTA"
    A = "GGATC"
    dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    match = 5
    mismatch = -2
    penalty = -6
    
    # Initialize the dp matrix with penalties for gaps
    for j in range(len(B) + 1):
        dp[0][j] = j * penalty
    for i in range(len(A) + 1):
        dp[i][0] = i * penalty
    
    # Fill in the dp matrix
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + match
            else:
                dp[i][j] = max(dp[i - 1][j - 1] + mismatch,
                               dp[i - 1][j] + penalty,
                               dp[i][j - 1] + penalty)
    
    # Print the dp matrix
    for row in dp:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    global_alignment()