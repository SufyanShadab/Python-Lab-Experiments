import re

doc = input("DOC (DD/MM/YY): ")

p = "From We bare bears i like Ice"

pattern = "bear"

# match (checking if string starts with "From")
r = re.match("From", p)
if r:
    print("valid start")
else:
    print("invalid start")

# search
r = re.search("bear", p)
if r:
    print("passphrase valid case 1")
else:
    print("passphrase invalid")

# findall
r = re.findall(pattern, p)
if r:
    print("passphrase valid case 2")
else:
    print("invalid passphrase")

# replace
v = re.sub("bear", "cat", p)
print(v)

# extract numbers (now using doc instead of id)
r = re.findall("[0-9]+", doc)
print(r)

# date validation
pattern = r"\d{2}/\d{2}/\d{2}$"
v = re.match(pattern, doc)

if v:
    print("valid DOC")
else:
    print("invalid DOC")