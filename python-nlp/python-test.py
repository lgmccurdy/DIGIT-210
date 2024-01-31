with open("lgm-chatgbt-results-2.txt", "r") as file:
    # Read the contents of the file
    file_contents = file.read()

    print(file_contents)

    import spacy

   # nlp = spacy.cli.download("en_core_web_sm")
    nlp = spacy.load('en_core_web_sm')

    text = "Amelia donned a leather aviator suit, her heart pounding with excitement and nervousness."
    doc = nlp(text)

    for token in doc:
        print(token.text, token.pos_, token.dep_)