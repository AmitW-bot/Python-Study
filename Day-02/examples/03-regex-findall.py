import re

text = "The quick brown fox"
pattern = r"brown"

findAll = re.findall(pattern, text)
if findAll:
    print("Pattern found:", findAll)
else:
    print("Pattern not found")
