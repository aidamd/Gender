import glob, spacy

female_cat = ["mother", "mothers", "mama", "mamas", "mom", "moms", "daughter", "daughters", "aunt", "aunts", "niece", "nieces", "grandmother", "grandmothers", "grandma", "grandmas", "queen", "queens", "princess", "princesses", "wife", "wifes", "bachelorette", "bachelorettes", "bride", "brides", "sister", "sister", "woman", "women", "girl", "girls", "madam", "madams", "she"]
male_cat = ["father", "fathers", "papa", "papas", "dad", "dads", "son", "sons", "uncle", "uncles", "nephew", "nephews", "grandfather", "grandfathers", "grandpa", "grandpas", "king", "kings", "prince", "princes", "husband", "husbands", "bachelor", "bachelors", "groom", "grooms", "brother", "brothers", "man", "men", "boy", "boys", "sir", "sirs", "he"]
SUBJECTS = ["nsubj"]
OBJECTS = ["dobj"]
nlp = spacy.load("en")


for txt in glob.glob("1960s/GilligansIsland/*"):
    print txt
    female_sub = 0
    female_obj = 0
    male_sub = 0
    male_obj = 0

    with open(txt, "rb") as file:
        content = file.readlines()
        all = ""
        if len(content) < 1:
            continue
        for line in content:
            if line.find(':') == 2:
                continue
            else:
                all += line.rstrip().lstrip().replace("??", "").replace("- ", "").replace(">>", "") + " "
        sentences = all.replace("-", "").replace(";", ".").replace("?", ".").replace("!",".").lower().split(".")
        for sentence in sentences:
            sentence = unicode(sentence, errors='ignore')
            doc = nlp(sentence)
            sub_toks = [tok for tok in doc if (tok.dep_ in SUBJECTS)]
            obj_toks = [tok for tok in doc if (tok.dep_ in OBJECTS)]
            for sub in sub_toks:
                sub = str(sub)
                zir_sub = sub.split(" ")
                for zir in zir_sub:
                    if zir in female_cat:
                        female_sub += 1
                    if zir in male_cat:
                        male_sub += 1
            for obj in obj_toks:
                obj = str(obj)
                zir_obj = obj.split(" ")
                for zir in zir_obj:
                    if zir in female_cat:
                        female_obj += 1
                    if zir in male_cat:
                        male_obj += 1
                if obj == "her" or obj == "hers":
                    female_obj += 1
                if obj == "him" or obj == "his":
                    male_obj += 1
        print txt
        print female_sub
        print male_sub
print "fin"
