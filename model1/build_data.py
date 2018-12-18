from nltk import pos_tag, word_tokenize
from nltk.tag.stanford import StanfordPOSTagger
import pickle
import re

# stanford_dir = '/Users/meetparekh/stanford-postagger-full-2018-10-16/'
# modelfile = stanford_dir + 'models/wsj-0-18-caseless-left3words-distsim.tagger'
# jarfile = stanford_dir + 'stanford-postagger-3.9.2.jar'

# st = StanfordPOSTagger(model_filename=modelfile, path_to_jar=jarfile)

filepath = "Tagged data.txt"
# start_date = "1996-01-01"
# end_date = "1996-12-31"

date_regex = re.compile('\d{4}-\d{2}-\d{2}')

data = []
labeled_data_subject = []

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
            # file.readline()
            subject = ""
            line = file.readline()
            if line[:-1] == 'Yes':
                subject = '1'
            else:
                subject = '0'
            labeled_data_subject.append((date, noun_list, subject))
            # print(line[:-1])
            line = file.readline()
            print(line[:-1])
            file.readline()
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
            title += line[:-1].lower()
            tokens = word_tokenize(title)
            tags = pos_tag(tokens)
            for tag in tags:
                if tag[1].startswith('NN'):
                    noun_list.append(tag[0])
                if tag[1].startswith('JJ') or tag[1].startswith('VB'):
                    adj_verb_list.append(tag[0])
        else:
            full_text += line.lower()
            tokens = word_tokenize(line.lower())
            tags = pos_tag(tokens)
            for tag in tags:
                if tag[1].startswith('NN'):
                    noun_list.append(tag[0])
                if tag[1].startswith('JJ') or tag[1].startswith('VB'):
                    adj_verb_list.append(tag[0])

print(labeled_data_subject)
# print(data)
#
# with open('data_obj', 'wb') as fp:
#     pickle.dump(data, fp)

with open('labeled_data', 'wb') as fp:
    pickle.dump(labeled_data_subject, fp)
