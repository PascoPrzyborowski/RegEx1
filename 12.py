# Task 1

import re
# Search for the first white-space character in the string

text = "Berlin is a world city of culture, politics, media and science."
x = re.search("\s", text)

print("The first white-space character is located in position:", x.start())

# Task 2

import re
# Make a search that returns no match

text="Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

x = re.search("Frankfurt", text)
print(x)

# Task 3

import re

# Replace a space with a hyphen

text = "Berlin is a city of culture."
x = re.sub("\s", "-", text)
print(x)

# Task 4

import re

# Search for a text in a string

text = "Berlin is a city of culture."
x = re.search("in", text)
print(x)

# Task 5
import re

# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "B":

text = "Berlin is a city of culture."
x = re.search(r"\bB\w+", text)
print(x.span())


# Task 6
import re

# Print the part of the string where there was a match.

text = "The rain in Spain"
x = re.findall("ai", text)
print(len(x))