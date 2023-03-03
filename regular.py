import re


pattern = r"[A-Z]$"

text = "lllllllllllls  aaaaaaaaaa AAAAAAAAAAAAAAAAAAAAAAAAAAAZBBBBBBBBBBBBBBBBBBBBBBBBBBBBB"

matches = re.finditer(pattern, text)
for match in matches:
    print(text[match.span()[0]:match.span()[1]])
