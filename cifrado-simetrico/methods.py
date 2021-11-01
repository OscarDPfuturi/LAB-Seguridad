def removeSpaces(mssg):
    mssg_len = len(mssg)
    mssg2 = []
    for i in range(mssg_len):
        if mssg[i] != ' ' and mssg[i] != '\n':
            mssg2.append(mssg[i])
    mssg2 = ''.join(mssg2)
    return mssg2