import glob, spacy, csv
from nltk.tokenize import word_tokenize

female_cat = ["mother", "mothers", "mama", "mamas", "mom", "moms", "daughter", "daughters", "aunt", "aunts", "niece", "nieces", "grandmother", "grandmothers", "grandma", "grandmas", "queen", "queens", "princess", "princesses", "wife", "wifes", "bachelorette", "bachelorettes", "bride", "brides", "sister", "sister", "woman", "women", "girl", "girls", "madam", "madams", "she"]
male_cat = ["father", "fathers", "papa", "papas", "dad", "dads", "son", "sons", "uncle", "uncles", "nephew", "nephews", "grandfather", "grandfathers", "grandpa", "grandpas", "king", "kings", "prince", "princes", "husband", "husbands", "bachelor", "bachelors", "groom", "grooms", "brother", "brothers", "man", "men", "boy", "boys", "sir", "sirs", "he"]
SUBJECTS = ["nsubj", "nsubjpass", "agent"]
OBJECTS = ["dobj", "iobj"]
nlp = spacy.load("en")

years = {}
with open('shows.csv', 'r') as csvfile1:
    spamreader = csv.reader(csvfile1)
    for row in spamreader:
        years[row[0]] = [row[1] + " " + row[2]]
    print years


with open('episodes.csv', 'wb') as csvfile:
    myFields = ['Show', 'Episode', 'Decade', 'Female_Sub', 'Female_Obj', 'Male_Sub', 'Male_Obj', 'Begin', 'End']
    spamwriter = csv.DictWriter(csvfile, fieldnames=myFields)
    spamwriter.writeheader()
    for i in range(1960, 2011, 10):
        for dir in glob.glob(str(i) + "s/*"):
            dirname = dir[6:]
            episode = 0
            for txt in glob.glob(dir + "/*"):
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
                                print sentence
                            if obj == "him" or obj == "his":
                                male_obj += 1
                                print sentence
                spamwriter.writerow({'Show': dirname, 'Episode': episode, 'Decade': str(i) , 'Female_Sub': female_sub, 'Female_Obj': female_obj, 'Male_Sub': male_sub, 'Male_Obj': male_obj, 'Begin': years[dirname][0].split(" ")[0], 'End' : years[dirname][0].split(" ")[1]})
                episode += 1
print "fin"
