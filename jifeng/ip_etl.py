import re


def proc():
    file = open("ip.txt", 'r', encoding='utf-8')
    lists = file.readlines()
    m = re.compile('\d+.\d+.\d+.\d+')
    for i in lists:
        # print(i)
        s = re.search('\d+\.\d+\.\d+\.\d+', i)
        if s:
            print(s.group())


proc()
