# URL Similarity By Sasan Azimi
# Version 0.1: use Levenshtein similarity
# The Levenshtein distance calculates the similarity between two strings based on the minimum number of 
# single-character edits (insertions, deletions, or substitutions) required to transform one string into anothe
# 
# Damerau-Levenshtein Distance: An extension of Levenshtein distance that allows for transpositions of adjacent characters12. It considers four types of operations: insertions, deletions, substitutions, and transpositions.

# Hamming Distance: Like Levenshtein but only works for strings of equal length2. 

# Jaro-Winkler Distance: Designed for short strings like names and considers character transpositions. It gives more favorable ratings to strings that match from the beginning2.
        # The Jaro similarity (simj) between two strings is defined as:

        # simj = 1/3 * ( m /|s1| + m/|s2| + (m-t)/m )

        # where:

        # m: Number of matching characters
        # Two characters from s1 and s2 are considered matching if they are the same and not farther than [max(|s1|, |s2|) / 2] – 1 characters apart.
        # |s1|, |s2|: The length of the first and second strings, respectively
        # t: Number of transpositions
        # Calculated as the number of matching (but different sequence order) characters divided by 2.

# Longest Common Subsequence (LCS): Finds the longest subsequence common to two sequences. It's useful for comparing strings where the order of characters matters.

# Smith-Waterman Algorithm: Originally developed for local sequence alignment in bioinformatics, it can be adapted for string similarity. It's particularly good at finding similar substrings within larger strings1.

import textdistance

print("\n")

url_1 = "https://bankmellat.ir/default.aspx"
url_1 = "https://bankmellat.ir"
url_2 = "https://bankmalat.ir"


# url_1="abcdefgh"
# url_2="abdcefgh"

# Using q-grams with Jaccard distance
levenshtein_distance = textdistance.levenshtein(url_1, url_2)
print("levenshtein_distance",levenshtein_distance)

dice_distance = textdistance.dice(url_1, url_2)  # by some difference, still 1!!
print("dice_distance",dice_distance)

jaro_winkler_distance = textdistance.jaro_winkler(url_1, url_2)
print("Jaro_distance",jaro_winkler_distance)

cosine_distance = textdistance.cosine.similarity(url_1, url_2)    # by some difference, still 1!!
print("cosine_distance",cosine_distance)

mlipns_distance = textdistance.mlipns(url_1, url_2)    # by some difference, still 1!!
print("mlipns_distance",mlipns_distance)

strcmp95_distance = textdistance.strcmp95(url_1, url_2)    # by some difference, still 1!!
print("strcmp95_distance",strcmp95_distance)

needleman_wunsch_distance = textdistance.needleman_wunsch(url_1, url_2)    # by some difference, still 1!!
print("needleman_wunsch_distance",needleman_wunsch_distance)


print("\n")
