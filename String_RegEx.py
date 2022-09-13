import re


#Task1

# text = "Berlin is a world city of culture, politics, media and science."
# pattern = r"(\s)"

# match = re.search(pattern, text)

# print("The first space charakter is located at position: ", match.start())


#Task2

# text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital. "

# pattern = r"(Frankfurt)"

# match = re.search(pattern, text)

# print(match)



#Task3

# text = "Berlin is a city of culture."

# match = re.sub('\s', '-', text)

# #match = re.sub(r"(?<=[A-Za-z])/s+(?=[A-Za-z])", "-", text)

# print(match)



#Task4

# text = "Berlin is a city of culture."

# pattern = r"(in)"

# match = re.search(pattern, text)

# print(match)




#Task 5

# text = " Berlin is a city of culture."

# pattern = r"(^[\s]*(?:\b[a-zA-Z]+\b[\s]*))"

# match = re.search(pattern, text)

# print(match)

# text = "Berlin is a city of culture."
# x = re.search(r"\bB\w+", text)
# print(x.span())


#Task6

# text = "The rain in Spain."

# x = re.findall("ai", text)
# print(len(x))