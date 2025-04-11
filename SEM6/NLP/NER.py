import nltk
import re
from nltk import word_tokenize, pos_tag, ne_chunk
from nltk.chunk import tree2conlltags
from nltk.corpus import stopwords

nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
nltk.download('stopwords')

def normalize_text(text):
    # Replace dates, currency, numbers
    text = re.sub(r'\d{1,2}[/-]\d{1,2}[/-]\d{2,4}', '<DATE>', text)
    text = re.sub(r'\$\d+(?:\.\d+)?', '<MONEY>', text)
    text = re.sub(r'\b\d+\b', '<NUMBER>', text)
    return text

def named_entity_recognition(text):
    tokens = word_tokenize(text)
    pos_tags = pos_tag(tokens)
    named_entities = ne_chunk(pos_tags)
    conll_tags = tree2conlltags(named_entities)

    entities = [(word, tag, ne) for word, tag, ne in conll_tags if ne != 'O']
    return entities

# Example usage
text = "Apple Inc. was founded on April 1, 1976. Tim Cook is the CEO. They earned $394 billion in 2022."

normalized = normalize_text(text)
entities = named_entity_recognition(normalized)

print("Normalized Text:", normalized)
print("Named Entities (word, POS, Entity):")
for entity in entities:
    print(entity)
