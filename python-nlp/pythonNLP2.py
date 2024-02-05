import spacy
nlp = spacy.load('en_core_web_md')

import os

workingDir = os.getcwd()

print("current working directory: " + workingDir)
insideDir = os.listdir(workingDir)

print("inside this directory are the following files AND directories: " + str(insideDir))

CollPath = os.path.join(workingDir, 'AI Experiments')
print(CollPath)

def readTextFiles(filepath):
    with open(filepath, 'r', encoding='utf8') as f:
        readFile = f.read()
        # print(readFile)
        stringFile = str(readFile)
        lengthFile = len(readFile)
        print(lengthFile)

        tokens = nlp(stringFile)
        vectors = tokens.vector

        wordOfInterest = nlp(u'between')
        print(wordOfInterest, ': ', wordOfInterest.vector_norm)


    highSimilarityDict = {}
    for token in tokens:
        if (token and token.vector_norm):
            # if token not in highSimilarityDict.keys(): # Alas, this did not work to remove duplicates from my dictionary. :-(
            if wordOfInterest.similarity(token) > .3:
                highSimilarityDict[token] = wordOfInterest.similarity(token)
                # The line above creates the structure for each entry in my dictionary.
                # print(token.text, "about this much similar to", wordOfInterest, ": ", wordOfInterest.similarity(token))

    sorted_dict = sorted(highSimilarityDict.items(),key=lambda x:x[1], reverse=True)
    highSimilarityDict = dict(sorted_dict)


    print("This is a dictionary of words most similar to the word " + wordOfInterest.text + " in this file.")
    print(highSimilarityDict)


    print("\n\n DICTIONARY COMPREHENSION TO DEDUPE THE DICTIONARY. "
          "\n I like this method because it's short and and whimsical."
          "\n It pulls a switcheroo! Keys become values in the first dictionary comprehension."
          "\n 'Deduping' happens because when a duplicate token is read as a *value* it is removed."
          "\n Then we reverse again and make the tokens be keys in the shorter dictionary."
          "Source: https://tutorial.eyehunts.com/python/python-remove-duplicates-from-dictionary-example-code/ ")
    switcheroo = {val: key for key, val in highSimilarityDict.items()}
    deduped = {val: key for key, val in switcheroo.items()}
    print(str(len(switcheroo)) + ' **** ' + f'{switcheroo=}')

    print(len(deduped), ' **** ', f'{deduped=}')
    print(len(deduped.items()), " vs ", len(highSimilarityDict.items()))


for file in os.listdir(CollPath):
    if file.endswith(".txt"):
        filepath = f"{CollPath}/{file}"
        print(filepath)
        readTextFiles(filepath)

