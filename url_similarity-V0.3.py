# URL Similarity By Sasan Azimi
# Version 0.3: After comparing several methods, we chose Jaro winkler method to calculate the similarity
# Jaro-Winkler Distance: Designed for short strings like names and considers character transpositions. It gives more favorable ratings to strings that match from the beginning2.
        # The Jaro similarity (simj) between two strings is defined as:

        # simj = 1/3 * ( m /|s1| + m/|s2| + (m-t)/m )

        # where:

        # m: Number of matching characters
        # Two characters from s1 and s2 are considered matching if they are the same and not farther than [max(|s1|, |s2|) / 2] – 1 characters apart.
        # |s1|, |s2|: The length of the first and second strings, respectively
        # t: Number of transpositions
        # Calculated as the number of matching (but different sequence order) characters divided by 2.

import textdistance

url_1 = "https://bankmellat.ir/default.aspx"
url_2 = "https://bankmalat.ir/abdcfdf/sdfdsf/12_sdfsdf"

split_url_1 = url_1.replace('https://','').split('/')
split_url_2 = url_2.split('/')


max_sim =0 
for token_1 in split_url_1:
    for token_2 in split_url_2:
        d = textdistance.jaro_winkler(token_1, token_2)
        if d> max_sim: max_sim = d
print(f"max similarity: {max_sim:.3f} ")
