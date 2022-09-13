import re

textsearched = "some text mail@mail.web.de some text in another one text"

pattern = r"(\w{3,3})"

x = re.search(pattern,textsearched)  
print(x)
print()
print(textsearched)
print()

# using the pattern to search the target text
#x = re.findall(pattern, text_to_be_searched)  
# printing out the match




#regex101r


#\w+(@)\w+(.)\w+  Wordchar +
#\S+\@\S+  Singelchar +