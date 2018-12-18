import nltk
import pickle
from collections import Counter
import os
import sys

data = []

with open('labeled_data', 'rb') as fp:
    data = pickle.load(fp)

print(len(data))

# with open('labeled_data_subject_2', 'rb') as fp:
#     data.extend(pickle.load(fp))

all_words = []

for row in data:
    for word in row[1]:
        all_words.append(word)

counter = Counter(all_words)

words_set = set([t[0] for t in counter.most_common(500)])

train_set = []
# word_counter = 0
for row in data:
    bag = {}
    for word in row[1]:
        if word in words_set:
            # word_counter += 1
            bag[word] = True
    output = ''
    if row[2] == '1':
        output = 'positive'
    else:
        output = 'negative'
    train_set.append((bag, output))


classifier = nltk.NaiveBayesClassifier.train(train_set)


with open('data_obj', 'rb') as fp:
    data_obj = pickle.load(fp)

i = len(data)-19
with open('rounds', 'rb') as fp:
    rounds = pickle.load(fp)
print(rounds)
# rounds = []
while i < len(data_obj):
    sample = []
    if i + 20 < len(data_obj):
        sample.extend(data_obj[i:i+20])
    else:
        sample.extend(data_obj[i:])

    dists = []
    features_list = []
    for row in sample:
        features = {}
        for word in row[2]:
            if word in words_set:
                features[word] = True
        dists.append(classifier.prob_classify(features))

    for j in range(len(dists)):
        dist = dists[j]
        output = ''
        for label in dist.samples():
            output += label + ' ' + str(dist.prob(label))
            output += ' | '
        print(output + " :: " + sample[j][0])

    k = input("Press any key to continue.")
    if str(k) == '1':
        break

    round_count = 0
    for j in range(len(dists)):
        dist = dists[j]
        l = ""
        # if dist.max() == 'negative'
        if dist.prob(dist.max()) < 0.9:
            round_count += 1
            os.system('clear')
            print(sample[j][0])
            print(sample[j][4])
            l = input('Is the article about microsoft? 0 for No, 1 for Yes :: ')
            # if str(l) == '2':
            #     with open('round_count', 'wb') as fp:
            #         pickle.dump(round_count, fp)
            #
            #     with open('labeled_data', 'wb') as fp:
            #         pickle.dump(data, fp)
            #     sys.exit()
        else:
            if(dist.max()) == 'positive':
                l = '1'
            else:
                l = '0'
        data.append((sample[j][1], sample[j][2], str(l)))

    rounds.append(round_count)

    all_words = []

    for row in data:
        for word in row[1]:
            all_words.append(word)

    counter = Counter(all_words)

    words_set = set([t[0] for t in counter.most_common(500)])

    train_set = []
    # word_counter = 0
    for row in data:
        bag = {}
        for word in row[1]:
            if word in words_set:
                # word_counter += 1
                bag[word] = True
        output = ''
        if row[2] == '1':
            output = 'positive'
        else:
            output = 'negative'
        train_set.append((bag, output))


    classifier = nltk.NaiveBayesClassifier.train(train_set)

    # break
    i += 20

with open('rounds', 'wb') as fp:
    pickle.dump(rounds, fp)

with open('labeled_data', 'wb') as fp:
    pickle.dump(data, fp)

# with open('sample_data', 'rb') as fp:
#     sample = pickle.load(fp)
#
# # print(word_counter)
#
# dists = []
# for row in sample:
#     features = {}
#     for word in row[2]:
#         if word in words_set:
#             features[word] = True
#     dists.append(classifier.prob_classify(features))
#
#
# for i in range(len(dists)):
#     dist = dists[i]
#     output = ''
#     for label in dist.samples():
#         output += label + ' ' + str(dist.prob(label))
#         output += ' | '
#     print(sample[i][0] + ' :: ' + output)
