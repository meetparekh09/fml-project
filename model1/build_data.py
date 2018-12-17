from nltk import pos_tag, word_tokenize
import pickle
import re

filepath = "../preprocessing/microsoft-sentence-split-new.txt"
# start_date = "1996-01-01"
# end_date = "1996-12-31"

date_regex = re.compile('\d{4}-\d{2}-\d{2}')

data = []


with open(filepath) as file:
    full_text = ""
    title = ""
    date = ""
    noun_list = []
    adj_verb_list = []

    for line in file:
        if line == "\n":
            data.append((title, date, noun_list, adj_verb_list, full_text))
            print("writing :: " + date + ", " + title)
            title = ""
            date = ""
            noun_list = []
            adj_verb_list = []
            full_text = ""
            # file.readline()
            continue
        elif date_regex.fullmatch(line[:-1]):
            print(line[:-1])
            date = line[:-1]
            # if date < start_date or date > end_date:
            # title = ""
            # date = ""
            # noun_list = []
            # adj_verb_list = []
            # full_text = ""
            # while file.readline() != "\n":
            #     continue
            # file.readline()
            # continue
        elif title == "":
            title += line[:-1]
        else:
            full_text += line
            tokens = word_tokenize(line)
            tags = pos_tag(tokens)
            for tag in tags:
                if tag[1].startswith('NN'):
                    noun_list.append(tag[0])
                if tag[1].startswith('JJ') or tag[1].startswith('VB'):
                    adj_verb_list.append(tag[0])

print(data)

with open('data_obj', 'wb') as fp:
    pickle.dump(data, fp)
