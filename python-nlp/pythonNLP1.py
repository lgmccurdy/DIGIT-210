import spacy

# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

# print text as wordstrings
chatgpt = open('lgm-chatgpt-results-2.txt', 'r', encoding='utf8')
words = chatgpt.read()
wordstrings = str(words)
print(wordstrings)



# process text
text = (wordstrings)
doc = nlp(text)
print()

# print verbs
print ("Verbs:")
for token in doc:
        if token.pos_ == "VERB":
            print(token.text)

# print verbs ending in "ing"

print ("Verbs ending in 'ing':")
for token in doc:
        if token.pos_ == "VERB" and token.text.endswith("ing"):
            print(token.text)

# print named entities
print("Named Entities:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")
