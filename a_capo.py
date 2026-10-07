# Open text file which contain the text
text_file_location = r"appunti.txt"
# Remove newline
with open(text_file_location, 'r') as file:
    text = file.read().replace('\n', '')

# Break up sentences by space
text_tokens = text.split(" ")
print(text_tokens)

# List of words that we do not want to split to newline
key_word = ["U.S.", "Mr.", "Mrs.", "U.S.A", "U.S"]
new_text_tokens = []

for x in text_tokens:
    if "." in x and x not in key_word:
        new_text_tokens.append(x + "\n")
    else:
        new_text_tokens.append(x + " ")

# Finally join back the word tokens, those words with \n will now cause the next sentence to be newlined.
# The rstrip() is to remove the last \n.
final_text = "".join(new_text_tokens).rstrip()

print("=======================================")
print(new_text_tokens)
print("=======================================")
print(final_text)