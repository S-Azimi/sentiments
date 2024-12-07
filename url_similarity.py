# URL Similarity By Sasan Azimi
# Version 0.1: use Levenshtein similarity
# The Levenshtein distance calculates the similarity between two strings based on the minimum number of 
# single-character edits (insertions, deletions, or substitutions) required to transform one string into anothe
# 

url_1 = "https://bankmellat.ir/"
url_2 = "https://bankmalat.ir"

url_1="abcdefghijklmno"
url_2="bac"



def levenshtein_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    
    return dp[m][n]

# Example usage
sentence1 = "The quick brown fox"
sentence2 = "The fast brown fox"

distance = levenshtein_distance(url_1, url_2)
print(f"Levenshtein distance: {distance}")