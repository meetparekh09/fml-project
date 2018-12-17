import corenlp
import sys
import re
import os

out_file = None

def separate_sentences(keywords, filepath, mode = 0):
    global out_file
    pattern = ''
    for word in keywords:
        pattern += '('+word+')|'
    pattern = pattern[:-1]
    # print(pattern)
    # return
    # pattern += ']'
    # print(pattern)
    with corenlp.CoreNLPClient(annotators="tokenize ssplit".split()) as client:
        with open(filepath) as file:
            i = 0
            text = ''
            headline = False
            for line in file:
                if i < 2:
                    if i == 0 and re.search(pattern, line, re.IGNORECASE):
                        headline = True
                    out_file.write(line)
                    i += 1
                    continue
                if line == '\n':
                    file.readline()
                    # print(text)
                    ann = client.annotate(text)

                    # print('\n\n\n')
                    # print('=================================================================')
                    for i in range(len(ann.sentence)):
                        # print(corenlp.to_text(ann.sentence[i]))
                        sentence = corenlp.to_text(ann.sentence[i])

                        if headline and mode == 0:
                            out_file.write(sentence+'\n')
                        elif re.search(pattern, sentence, re.IGNORECASE):
                            out_file.write(sentence+'\n')

                    out_file.write('\n\n')
                    # print('=================================================================')
                    # print('\n\n\n')
                    text = ''
                    headline = False
                    i = 0
                    continue
                text += line


if __name__ == '__main__':
    if len(sys.argv) >= 2 and isinstance(sys.argv[1], str):
        # print(sys.argv[1])
        out_file = open(sys.argv[1], 'w')
        filelist = os.listdir(sys.argv[2])
        filelist.sort()
        for filename in filelist:
            if filename.endswith(".txt"):
                filepath = os.path.join(sys.argv[2], filename)
                mode = 0
                if re.search('factiva', filename, re.IGNORECASE):
                    mode = 1
                separate_sentences(sys.argv[3:], filepath, mode)
        out_file.close()
        # print(sys.argv[1:])
