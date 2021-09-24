import wikipedia

# select language
wikipedia.set_lang("tr")

# Type what you want to search
elon_musk = wikipedia.search("Elon Musk")

result = wikipedia.summary(elon_musk[0])

print(result)
