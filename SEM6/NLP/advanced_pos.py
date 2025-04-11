import spacy
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser


# Load spaCy models
nlp = spacy.load("en_core_web_sm")

# Function for NLP processing
def process_text(text, lang="en"):
    doc = nlp(text)
    print("\nPOS Tags:")
    for t in doc:
        print(f"{t.text} -> {t.pos_}")
    
    print("\nSyntactic Dependencies:")
    for t in doc:
        print(f"{t.text} -> {t.dep_} -> {t.head.text}")
    
    print("\nExtracted Noun Phrases:")
    for chunk in doc.noun_chunks:
        print(chunk.text)
    
    print("\nNamed Entities:")
    for ent in doc.ents:
        print(f"{ent.text} -> {ent.label_}")
    
    return doc

# Noun phrase extraction using NLTK
def extract_phrases(text):
    pos_tags = pos_tag(word_tokenize(text))
    grammar = r"NP: {<DT>?<JJ>*<NN.*>+}"
    tree = RegexpParser(grammar).parse(pos_tags)

    print("\nNoun Phrases:")
    for subtree in tree.subtrees():
        if subtree.label() == "NP":
            phrase = " ".join(word for word, tag in subtree.leaves())
            print(phrase)

# Sample usage
text = "Barack Obama was the 44th President of the US"
doc = process_text(text, "en")
extract_phrases(text)
