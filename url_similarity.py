# URL Similarity By Sasan Azimi
# Version 0.1: in the first version I'm trying to compare diferent similariy methods
# 

url_1 = "https://bankmellat.ir/default.aspx"
url_2 = "https://bankmelat.ir"


import spacy

nlp = spacy.load("en_core_web_md")
doc1 = nlp("The bottle is empty")
doc2 = nlp("There is nothing in the bottle")
similarity = doc1.similarity(doc2)
print(f"Similarity: {similarity}")

