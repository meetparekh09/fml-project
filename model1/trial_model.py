import pickle
import random

with open('data_obj', 'rb') as fp:
    data = pickle.load(fp)


microsoft_data = []
other_data = []

for row in data:
    if 'microsoft' in row[0]:
        microsoft_data.append(row)
    else:
        other_data.append(row)


print(len(microsoft_data))
print(len(other_data))

random.shuffle(microsoft_data)
random.shuffle(other_data)

bootstrap_data = microsoft_data[:10]
bootstrap_data.extend(other_data[:10])
random.shuffle(bootstrap_data)
labeled_data_subject = []
labeled_data_sentiment = []

# with open('to_be_tagged.txt', 'w') as file:
#     for row in bootstrap_data:
#         file.write(row[0]+'\n')
#         file.write(row[1]+'\n')
#         for line in row[4]:
#             file.write(line)
#         file.write('\n\n')


# for row in bootstrap_data[:5]:
#     print("\n")
#     print("=========================================================================================================")
#     print(row[0])
#     print(row[1])
#     print(row[4])
#     print("=========================================================================================================")
#     print("\n")
#     subject = input("Is this article primarily about Microsoft? 0 - No, 1 - Yes :: ")
#     sentiment = input("Is this article positive, negative or neutral? 1 - Positive, 0 - Neutral, -1 - Negative")
#     labeled_data_subject.append((row[1], row[2], subject))
#     labeled_data_sentiment.append((row[1], row[3], sentiment))
#
#
# with open('labeled_data_subject', 'wb') as fp:
#     pickle.dump(labeled_data_subject, fp)
#
# with open('labeled_data_sentiment', 'wb') as fp:
#     pickle.dump(labeled_data_sentiment, fp)
