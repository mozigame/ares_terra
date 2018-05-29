def proc():
    file = open('f', 'r')
    lists = file.readlines()
    for l in lists:
        print("'{}',".format(l.strip().split(',')[1]))


proc()
