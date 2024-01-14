import stanza
stanza.download('en') # download English model
nlp = stanza.Pipeline('en') # initialize English neural pipeline
doc = nlp("Barack Obama was born in Hawaii.") # run annotation over a sentence

print(doc)
print(doc.entities)
doc.sentences[0].print_dependencies()
