import spacy
from nltk.tokenize import word_tokenize

female_cat = ["mother", "mama", "mom", "daughter", "aunt", "niece", "grandmother", "grandma", "queen", "princess", "wife", "bachelorette", "bride", "sister", "woman", "girl", "madam"]
male_cat = ["father", "papa", "dad", "son", "uncle", "nephew", "grandfather", "grandpa", "king", "prince", "husband", "bachelor", "groom", "brother", "man", "boy", "sir"]

SUBJECTS = ["nsubj"]
OBJECTS = ["dobj"]

frequency = {}
female_sub = {}
female_obj = {}
male_sub = {}
male_obj = {}

for fe in female_cat:
    frequency[fe] = 0
    female_obj[fe] = 0
    female_sub[fe] = 0
for me in male_cat:
    frequency[me] = 0
    male_obj[me] = 0
    male_sub[me] = 0

female_dep = {}
male_dep = {}
nlp = spacy.load("en")

female_count = 0
male_count = 0
with open("Scripts/2010.txt", "rb") as file:
    content = file.readlines()
    for line in content:
        sentences = line.replace("-", "").replace(";", ".").replace("?", ".").replace("!", ".").lower().split(".")
        for sentence in sentences:
            for word in frequency.keys():
                if word in sentence:
                    frequency[word] += 1
            sentence = unicode(sentence, errors='ignore')
            doc = nlp(sentence)
            for tok in doc:
                tok_st = str(tok)
                if tok_st in female_cat:
                    if tok.dep_ in female_dep.keys():
                        female_dep[tok.dep_] += 1
                    else:
                        female_dep[tok.dep_] = 1
                elif tok_st in male_cat:
                    if tok.dep_ == "npadvmod":
                        print sentence
                    if tok.dep_ in male_dep.keys():
                        male_dep[tok.dep_] += 1
                    else:
                        male_dep[tok.dep_] = 1
print female_dep
print male_dep
