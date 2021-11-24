# Initial Paragraph
string = "Never give in — Never, never, never, never, in nothing great or small, large or petty, never give in except to convictions of honour and good sense. Never yield to force; never yield to the apparently overwhelming might of the enemy. O horror, horror, horror. Words, words, word. But you never know now do you now do you now do you."

# Dictionary to be used later
dictionary = {}

# Make string all lower case
string = string.lower()

# Special Characters to remove
no_chars = ",.—"

# Remove those characters from string
for char in no_chars:
    string = string.replace(char,"")

# Make the string into a list
lst = sorted(string.split())

# Loop through list counting each word and placing as value to each key word
for word in lst:
    dictionary[word] = lst.count(word)

# Printing output using formating
print("\n".join(" {:10} \t{} ".format(x, y) for x, y in dictionary.items()))