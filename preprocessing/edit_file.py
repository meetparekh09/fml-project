import re

date_regex = re.compile('\d{4}-\d{2}-\d{2}')

start_date = "1996-01-01"
end_date = "1996-12-31"

def getMonthNumber(mon):
    if mon == 'Jan' or mon == 'January':
        return '01'
    if mon == 'Feb' or mon == 'February':
        return '02'
    if mon == 'Mar' or mon == 'March':
        return '03'
    if mon == 'Apr' or mon == 'April':
        return '04'
    if mon == 'May':
        return '05'
    if mon == 'Jun' or mon == 'June':
        return '06'
    if mon == 'Jul' or mon == 'July':
        return '07'
    if mon == 'Aug' or mon == 'August':
        return '08'
    if mon == 'Sep' or mon == 'September':
        return '09'
    if mon == 'Oct' or mon == 'October':
        return '10'
    if mon == 'Nov' or mon == 'November':
        return '11'
    if mon == 'Dec' or mon == 'December':
        return '12'

headline = ''
date = ''
body = ''
with open('microsoft-sentence-split.txt') as file:
    with open('microsoft-sentence-split-new.txt', 'w') as write_file:
        for line in file:
            if line == '\n':
                if date and date >= start_date and date <= end_date:
                    print("Writing :: " + date + ", " + headline)
                    write_file.write(date)
                    write_file.write(headline)
                    write_file.write(body)
                    write_file.write('\n')
                headline = ''
                date = ''
                body = ''
                continue
            elif headline == '' and date_regex.fullmatch(line[:-1]) is None:
                headline = line
            elif date == '' and date_regex.fullmatch(line[:-1]) is not None:
                date = line
            elif date == '' and line.startswith('Publication date:'):
                date = line[:-1].split(':')[1].strip()
                # print(getMonthNumber(date.split(',')[0].split(' ')[0]))
                try:
                    mon = getMonthNumber(date.split(',')[0].split(' ')[0])
                    day = date.split(',')[0].split(' ')[1]
                    if len(day) == 1:
                        day = '0'+day
                    year = date.split(',')[1].split(' ')[1]
                    if len(year) != 4:
                        print(headline)
                except:
                    date = None
                    continue
                # print(year)
                # print(mon)
                # print(day)

                date = str(year) + '-' + str(mon) + '-' + str(day) + '\n'
                # print(date)
            else:
                body += line
