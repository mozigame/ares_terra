import os


def calc_log_line():
    file_path = "{}{}log{}a".format(os.getcwd(), os.sep, os.sep)

    file = open(file_path, 'r')
    nums = file.readlines()

    faileds = []
    for i in range(0, nums.__len__() - 1):
        if nums[i].strip() == '':
            continue
        t = int(nums[i].strip())
        v = int(nums[i + 1].strip())
        if (v - t) != 1:
            print(v, t)
            faileds.append(v)

    print()
    print(faileds)
    print(faileds.__len__())


calc_log_line()
