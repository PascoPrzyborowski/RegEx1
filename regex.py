import re


text = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""

# pattern = r"(\w+@\w+.\w+)"

#x = re.search(pattern,text) 

# email = "therealjeffbezos@bossnet.com"

# pattern1 = re.compile('\w+@\w+.\w+')
# matchResult = pattern1.search(email)
# if matchResult:
#     print(matchResult.group(1))
# else:
#     print("shit")

# mydog = re.compile(', (.*?)\n')
# >>> matchResult = mydog.search(s)
# >>> if matchResult:
#         print(matchResult.group(1))

findmeone = r"(\w+@\w+.\w+)"

pat = r"(\\b[a-z]{2}\\b)"
pat1 = r"(\t Sry \t)"
pat2 = r"(\S\w{4}\S)"
pat3 = r"(\\b[a-z]{3}\\b)"
pat4 = r"(\\b[a-z]{4}\\b)"


matchmesome = re.search(findmeone, text)
matchmesome1 = re.findall(findmeone, text)

res1 = re.search(pat, text)
res2 = re.findall(pat, text)

res3 = re.search(pat1, text)
res4 = re.findall(pat1, text)

res5 = re.search(pat2, text)
res6 = re.findall(pat2, text)

res7 = re.findall(pat3, text)
res8 = re.split(pat4, text)
res9 = re.sub(pat2,"ME", text)

print()
print(matchmesome)
print()
print(matchmesome1)
print()
print(res1)
print()
print(res2)
print()
print(res3)
print()
print(res4)
print()
print(res5)
print()
print(res6)
print()
print(res7)
print()
print(res8)
print()
print(res9)
print()


# print(text)
# print()
# print(match)
# print()
