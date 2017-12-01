def aocinput(day):
    "Opens todays' input file."
    filename = 'input/{}.txt'.format(day)
    filename = open(filename)
    filename = filename.read()
    return filename
