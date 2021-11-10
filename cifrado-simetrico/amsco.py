LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('mensaje.txt','r',encoding='utf-8')
    mssg = file.read()
    file.close()
    mssg = removeSpaces(mssg)
    key = input("Ingrese la clave: ")
    ciphertext = amsco(mssg, key.upper())
    print("Texto cifrado:", ciphertext)

def removeSpaces(mssg):
    mssg_len = len(mssg)
    mssg2 = []
    for i in range(mssg_len):
        if mssg[i] != ' ' and mssg[i] != '\n':
            mssg2.append(mssg[i])
    mssg2 = ''.join(mssg2)
    return mssg2

def splittingMessage(mssg, ncol):
    mssg_len = len(mssg)
    mat = []
    ngram = 1
    i = 0
    print(mssg_len)
    while i < mssg_len:
        row = []
        for j in range(ncol):
            if ngram == 1:
                if i < mssg_len:
                    row.append(mssg[i])
                else :
                    row.append('_')
                ngram = 2; i+=1
            else :
                if mssg_len - i == 1:
                    row.append(mssg[i] + '_')
                elif mssg_len - i > 1:
                    row.append(mssg[i:i+2])
                else :
                    row.append('__')
                ngram = 1;
                i+=2
        if ncol%2 == 0:
            if ngram == 1: ngram = 2
            else : ngram = 1
        mat.append(row)
    return mat

def printMat(mssg):
    print("Mensaje dividido:")
    for i in range(len(mssg)):
        print(mssg[i])

def amsco(mssg, key):
    key_len = len(key)
    nkey = []
    for i in range(key_len):
        nkey.append(LETRAS.find(key[i]))
    nkey2 = sorted(nkey)
    mssg = splittingMessage(mssg, key_len)
    printMat(mssg)
    mssg_rows = len(mssg)
    ciphertext = []
    for i in range(key_len):
        column = nkey.index(nkey2[i])
        for j in range(mssg_rows):
            if mssg[j][column] != None:
                ciphertext.append(mssg[j][column])
    ciphertext = ''.join(ciphertext)
    return ciphertext

if __name__ == '__main__' :
    main()
