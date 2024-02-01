import spacy

# nlp = spacy.cli.download("en_core_web_sm")
nlp = spacy.load('en_core_web_sm')

chatgbt = open('lgm-chatgbt-results-2.txt', 'r', encoding='utf8')
words = chatgbt.read()
wordstrings = str(words)
print(wordstrings)




text = "Amelia donned a leather aviator suit, her heart pounding with excitement and nervousness."
doc = nlp(text)

for token in doc:
    print(token.text, token.pos_, token.dep_)