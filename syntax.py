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
            sub_toks = [tok for tok in doc if (tok.dep_ in SUBJECTS) ]
            obj_toks = [tok for tok in doc if (tok.dep_ in OBJECTS) ]
            for sub in sub_toks:
                sub = str(sub)
                zir_sub = sub.split(" ")
                for zir in zir_sub:
                    if zir in female_cat:
                        female_sub[zir] += 1
                        female_count += 1
                    if zir in male_cat:
                        male_sub[zir] += 1
                        male_count += 1
            for obj in obj_toks:
                obj = str(obj)
                zir_obj = obj.split(" ")
                for zir in zir_obj:
                    if zir in female_cat:
                        female_obj[zir] += 1
                        female_count += 1
                    if zir in male_cat:
                        male_obj[zir] += 1
                        male_count += 1
print female_count
print male_count
for m in male_cat:
    print m
    print male_sub[m]
    print male_obj[m]
    print frequency[m]
for f in female_cat:
    print f
    print female_sub[f]
    print female_obj[f]
    print frequency[f]