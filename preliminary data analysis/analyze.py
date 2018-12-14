import os
import re

count = 0
microsoftHeadlineCount = 0
associatedHeadlineCount = 0
yearCount = {}
microsoftYearCount = {}
writeFile = open('./proquest-wsj-merged-file.txt', 'w')

companyName = 'Microsoft'

def getMonthNumber(mon):
    if mon == 'Jan' or mon == 'January':
        return 1
    if mon == 'Feb' or mon == 'February':
        return 2
    if mon == 'Mar' or mon == 'March':
        return 3
    if mon == 'Apr' or mon == 'April':
        return 4
    if mon == 'May':
        return 5
    if mon == 'Jun' or mon == 'June':
        return 6
    if mon == 'Jul' or mon == 'July':
        return 7
    if mon == 'Aug' or mon == 'August':
        return 8
    if mon == 'Sep' or mon == 'September':
        return 9
    if mon == 'Oct' or mon == 'October':
        return 10
    if mon == 'Nov' or mon == 'November':
        return 11
    if mon == 'Dec' or mon == 'December':
        return 12

filelist = os.listdir("../../"+companyName+"/The Wall Street Journal")
filelist.sort()
for filename in filelist:
    if filename.endswith(".txt"):
        # print(os.path.join("../../Microsoft/The Wall Street Journal", filename))
        filepath = os.path.join("../../"+companyName+"/The Wall Street Journal", filename)

        startOfArticle = False
        bodyStart = False
        bodyEnd = True
        endOfArticle = True
        headline = ''
        body = ''
        date = ''

        with open(filepath) as file:
            # file.readline()
            for line in file:
                if line == '____________________________________________________________\n':
                    startOfArticle = not startOfArticle
                    endOfArticle = not endOfArticle
                if line == '\n':
                    continue
                if endOfArticle:
                    count += 1
                    writeFile.write(headline)
                    writeFile.write(date)
                    writeFile.write(body)
                    writeFile.write('\n\n')
                    # print(headline)
                    if 'Microsoft' in headline or 'Microsoft' in headline:
                        microsoftHeadlineCount += 1

                    if 'Microsoft' in headline or 'Microsoft' in headline:
                        associatedHeadlineCount += 1
                        if date != '':
                            year = int(date[-6:].replace(" ", ""))
                            if year in microsoftYearCount.keys():
                                microsoftYearCount[year] += 1
                            else:
                                microsoftYearCount[year] = 1
                            actualDate = ''.join(' '.join(date.split(' ')[2:]).split(','))
                            # print(year)
                    # print(body)
                    # print(date)

                    if date != '':
                        year = int(date[-6:].replace(" ", ""))
                        if year not in yearCount.keys():
                            yearCount[year] = 1
                        else:
                            yearCount[year] += 1
                        # if year not in yearCount.keys():
                        #     yearCount[year] = {}
                        #
                        actualDate = ''.join(' '.join(date.split(' ')[2:]).split(','))
                        actualDate = actualDate.replace(" ", "")
                        # print(date)
                        # print(actualDate)
                        mon = getMonthNumber(actualDate[0:3])

                        # if mon not in yearCount[year].keys():
                        #     yearCount[year][mon] = 1
                        # else:
                        #     yearCount[year][mon] += 1

                        # print(date)
                        # print(mon)

                        day = -1
                        if len(actualDate) == 9:
                            day = int(actualDate[3])
                        else:
                            day = int(actualDate[3:5])

                        date = ''
                        date += str(year)+'-'
                        if mon < 10:
                            date += '0'+str(mon)
                        else:
                            date += str(mon)

                        date += '-'

                        if day < 10:
                            date += '0'+str(day)
                        else:
                            date += str(day)
                        # print(date)

                    headline = ''
                    body = ''
                    date = ''
                    endOfArticle = False
                    startOfArticle = True

                    # try:
                    #     year = int(s.split(',')[-1].replace(" ", ""))
                    #     print(year)
                    # except:
                    #     continue

                    continue

                if startOfArticle and line != '\n' and line != '____________________________________________________________\n' and headline == '':
                    headline = line
                if startOfArticle and line.startswith('Full text:'):
                    bodyStart = True
                    bodyEnd = False
                if startOfArticle and (line.startswith('Credit:') or line.startswith('Title:')) or line.startswith('Subject:'):
                     bodyStart = False
                     bodyEnd = True

                if startOfArticle and line.startswith('Publication date:'):
                    date = line

                if startOfArticle and bodyStart:
                    body += line

# print(count)
# print(microsoftHeadlineCount)
# print(associatedHeadlineCount)
#
# print(yearCount)
# print(microsoftYearCount)
writeFile.close()


writeFile = open('./factiva-wsj-merged-file.txt', 'w')
def checkHeadlineCondition(line):
    return not (line == '' or line.startswith('Opinion Journal;') or line == 'Factiva' or line == 'Dow Jones' \
    or line == 'Tech' or line == 'AWSJ' or line == 'Markets' or line == 'WSJE' or line == 'Business' \
    or line == 'Real Estate' or line == 'Heard on the Street' or line == 'Personal Technology' or line == 'US'\
    or line == 'Personal Finance' or line == 'World News' or line == 'Small Business' \
    or line == 'Investing in Funds' or line == 'Technology' or line == 'Opinion' or line == 'Advertising' \
    or line == 'R.O.I.' or line == "Today's Markets" or line == 'Credit Markets' or line == 'India News' \
    or line == "Mossberg's Mailbox" or line == 'The Mossberg Solution'\
    or line == "Investor's Calendar" or line == 'Theory & Practice' or line == 'Common Sense'\
    or line == 'Europe Markets' or line == 'Options' or line == 'Europe News' or line == 'Long Toss'\
    or line == 'Ahead of the Tape' or line == 'Gadgets' or line == 'Asia 200' or line == 'Fund Track' \
    or line == 'Writing on the Wall' or line == 'Large Stock Focus' or line == 'General News' or line == 'Special'\
    or line == 'Remembrances' or line == 'Politics and Policy' or line == 'News' or line == 'Corrections'\
    or line == 'Markets Main' or line == 'Boss Talk' or line == 'Letters' or line == 'Health' or line == 'Careers' \
    or line == 'India Journal' or line == 'Opinion Europe' or line == 'The Intelligent Investor' \
    or line == 'Investing' or line == 'Tech Journal' or line == 'Business Technology' or line == 'Asia News'\
    or line == 'Abreast of the Market' or line == 'Europe' or line == 'Management' or line == 'Guest Column'\
    or line == 'San Francisco Bay Area' or line == 'Travel Watch' or line == 'Small Stock Focus'\
    or line == 'World Stock Markets' or line == 'U.S. News' or line == 'Asia Technology' \
    or line == 'Weekend Investor' or line == 'ROI' or line == 'Running a Business' or line == 'The Middle Seat'\
    or line == 'Autos' or line == 'Deal of the Week' or line == 'Law' or line == 'Asia Business'\
    or line == 'Media & Marketing' or line == 'Managing in Asia' or line == 'Europe Technology' \
    or line == 'Sports' or line == 'Earnings' or line == 'Business World' or line == 'What They Know' \
    or line == 'India Business' or line == 'IPOs' or line == "This Week's Tip" or line == 'Your Executive Career'\
    or line == 'Money' or line == 'Getting Going' or line == 'Deals & Deal Makers' or line == 'World'\
    or line == 'Main Street' or line == 'New York' or line == 'Politics' or line == 'Autos Industry'\
    or line == 'Agenda' or line == 'The Money Hunt' or line == 'Year-End Review' or line == 'Sunday Journal'\
    or line == 'ECO:nomics' or line == 'Photos' or line == 'Deals India' or line == 'Information Age'\
    or line == 'Upside' or line == 'Invest' or line == 'US Page One' or line == 'The Digital Solution' \
    or line == 'Life and Style' or line == 'Reply to All' or line == 'Decos and Corrections'\
    or line == 'Work & Family' or line == 'Tech Europe' or line == 'Interactives' or line == 'The Numbers Guy'\
    or line == 'Analyse' or line == 'The Commish' or line == "Al's Emporium" or line == 'Next in Tech' \
    or line == 'Asia' or line == 'Travel' or line == 'Life' or line == 'Mobile'\
    or line == 'Personal Technology: Review' or line == 'Pro Private Markets' or line == 'Page One'\
    or line == 'Pro Cyber' or line == 'U.S. Markets' or line == 'Economy' or line == 'Brussels Beat'\
    or line == 'Your Health')


# count = 0
# microsoftHeadlineCount = 0
# associatedHeadlineCount = 0
# yearCount = {}
# microsoftYearCount = {}

filelist = os.listdir("../../"+companyName+"/The Wall Street Journal Factiva")
dateRegex = re.compile('[1-3]?[0-9] [a-zA-Z]* 20[0-1][0-9]')
bodyStartRegex = re.compile('(Copyright [0-9]{4} Dow Jones & Company, Inc. All Rights Reserved.)|(Copyright \\(c\\) [0-9]{4}, Dow Jones & Company, Inc.)')
filelist.sort()
for filename in filelist:
    fileString = ''
    if filename.endswith(".txt"):
        # print(os.path.join("../../Microsoft/The Wall Street Journal", filename))
        filepath = os.path.join("../../"+companyName+"/The Wall Street Journal Factiva", filename)

        with open(filepath) as file:
            for line in file:
                fileString += line

            prevLoc = 0
            loc = fileString.find('\n\n\n')
            while loc < len(fileString):
                article = fileString[:loc]
                headline = ''
                date = ''
                body = ''
                bodyStart = False
                for line in article.split('\n'):
                    # print('================================================')
                    # print(line)
                    # input()
                    if line == '':
                        continue
                    if headline == '' and checkHeadlineCondition(line):
                        headline = line
                    if date == '' and (dateRegex.fullmatch(line) is not None):
                        date = line

                    if (not bodyStart) and (bodyStartRegex.fullmatch(line) is not None):
                        bodyStart = True
                        continue
                    if (bodyStart) and line == 'Dow Jones & Company, Inc.':
                        bodyStart = False
                        continue
                    if bodyStart:
                        body += line+'\n'
                # print(headline)
                # print(date)
                # print(body)
                if 'Microsoft' in headline or 'Microsoft' in headline:
                    associatedHeadlineCount += 1
                    if date != '':
                        year = int(date[-5:].replace(" ", ""))
                        if year in microsoftYearCount.keys():
                            microsoftYearCount[year] += 1
                        else:
                            microsoftYearCount[year] = 1
                if 'Microsoft' in headline or 'Microsoft' in headline:
                    microsoftHeadlineCount += 1



                if date != '':
                    splitDate = date.split(' ')
                    year = int(splitDate[2])
                    mon = getMonthNumber(splitDate[1])
                    day = int(splitDate[0])

                    if year not in yearCount.keys():
                        yearCount[year] = 1
                    else:
                        yearCount[year] += 1
                    # if year not in yearCount.keys():
                        # yearCount[year] = {}

                    # if mon not in yearCount[year].keys():
                    #     yearCount[year][mon] = 1
                    # else:
                    #     yearCount[year][mon] += 1

                    date = ''
                    date += str(year)+'-'
                    if mon < 10:
                        date += '0'+str(mon)
                    else:
                        date += str(mon)

                    date += '-'

                    if day < 10:
                        date += '0'+str(day)
                    else:
                        date += str(day)
                    # print(date)
                    # print(year)
                count += 1

                writeFile.write(headline+'\n')
                writeFile.write(date+'\n')
                writeFile.write(body)
                writeFile.write('\n\n')
                # input()
                fileString = fileString[loc+3:]
                loc = fileString.find('\n\n\n')
                if loc == -1:
                    break
#
# print(count)
# print(microsoftHeadlineCount)
# print(associatedHeadlineCount)
# print(yearCount)
# print(microsoftYearCount)

writeFile.close()


writeFile = open('./proquest-nytimes-merged-file.txt', 'w')
filelist = os.listdir("../../"+companyName+"/The New York Times")
filelist.sort()
for filename in filelist:
    if filename.endswith(".txt"):
        # print(os.path.join("../../Microsoft/The New York Times", filename))
        filepath = os.path.join("../../"+companyName+"/The New York Times", filename)

        startOfArticle = False
        bodyStart = False
        bodyEnd = True
        endOfArticle = True
        headline = ''
        body = ''
        date = ''

        with open(filepath) as file:
            # file.readline()
            for line in file:
                if line == '____________________________________________________________\n':
                    startOfArticle = not startOfArticle
                    endOfArticle = not endOfArticle
                if line == '\n':
                    continue
                if endOfArticle:
                    count += 1
                    writeFile.write(headline)
                    writeFile.write(date)
                    writeFile.write(body)
                    writeFile.write('\n\n')
                    # print(headline)
                    if 'Microsoft' in headline or 'Microsoft' in headline:
                        microsoftHeadlineCount += 1

                    if 'Microsoft' in headline or 'Microsoft' in headline:
                        associatedHeadlineCount += 1
                        if date != '':
                            year = int(date[-6:].replace(" ", ""))
                            if year in microsoftYearCount.keys():
                                microsoftYearCount[year] += 1
                            else:
                                microsoftYearCount[year] = 1
                            # print(year)
                    # print(body)
                    # print(date)

                    if date != '':
                        year = int(date[-6:].replace(" ", ""))
                        # if year not in yearCount.keys():
                        #     yearCount[year] = {}
                        if year not in yearCount.keys():
                            yearCount[year] = 1
                        else:
                            yearCount[year] += 1

                        actualDate = ''.join(' '.join(date.split(' ')[2:]).split(','))
                        actualDate = actualDate.replace(" ", "")
                        # print(date)
                        # print(actualDate)
                        mon = getMonthNumber(actualDate[0:3])

                        # if mon not in yearCount[year].keys():
                        #     yearCount[year][mon] = 1
                        # else:
                        #     yearCount[year][mon] += 1

                        # print(date)
                        # print(mon)

                        day = -1
                        if len(actualDate) == 9:
                            day = int(actualDate[3])
                        else:
                            day = int(actualDate[3:5])

                        date = ''
                        date += str(year)+'-'
                        if mon < 10:
                            date += '0'+str(mon)
                        else:
                            date += str(mon)

                        date += '-'

                        if day < 10:
                            date += '0'+str(day)
                        else:
                            date += str(day)
                        # print(date)

                    headline = ''
                    body = ''
                    date = ''
                    endOfArticle = False
                    startOfArticle = True

                    # try:
                    #     year = int(s.split(',')[-1].replace(" ", ""))
                    #     print(year)
                    # except:
                    #     continue

                    continue

                if startOfArticle and line != '\n' and line != '____________________________________________________________\n' and headline == '':
                    headline = line
                if startOfArticle and line.startswith('Full text:'):
                    bodyStart = True
                    bodyEnd = False
                if startOfArticle and (line.startswith('Credit:') or line.startswith('Title:')) or line.startswith('Subject:'):
                     bodyStart = False
                     bodyEnd = True

                if startOfArticle and line.startswith('Publication date:'):
                    date = line

                if startOfArticle and bodyStart:
                    body += line

print(count)
print(microsoftHeadlineCount)
print(associatedHeadlineCount)
print(yearCount)
print(microsoftYearCount)
writeFile.close()

# for k, _ in yearCount.items():
#     for key, value in yearCount[k].items():
#         print(str(k)+','+str(key)+','+str(value))
