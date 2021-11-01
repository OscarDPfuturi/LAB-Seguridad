import methods as met

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('mensaje.txt','r',encoding='utf-8')
    mssg = file.read()
    file.close()
    mssg = met.removeSpaces(mssg)
    key = input("Ingrese la clave: ")
    #splittingMessage(mssg)
    ciphertext = amsco(mssg, key.upper())
    print(ciphertext)

def splittingMessage(mssg):
    mssg_len = len(mssg)
    mat = []
    ngram = 1
    i = 0
    while i < mssg_len:
        row = []
        for j in range(5):
            row.append(mssg[i:i+ngram])
            if ngram == 1: ngram = 2; i+=1
            else : ngram = 1; i+=2
        mat.append(row)
    return mat

def amsco(mssg, key):
    key_len = len(key)
    nkey = []
    for i in range(key_len):
        nkey.append(LETRAS.find(key[i]))
    print(nkey)
    nkey2 = sorted(nkey)
    print(nkey2)
    #nkey2 = ''.join(nkey2)
    mssg = splittingMessage(mssg)
    mssg_rows = len(mssg)
    print(mssg)
    ciphertext = []
    for i in range(key_len):
        column = nkey.index(nkey2[i])
        print(column)
        for j in range(mssg_rows):
            if mssg[j][column] != None:
                ciphertext.append(mssg[j][column])
    ciphertext = ''.join(ciphertext)
    return ciphertext

if __name__ == '__main__' :
    main()
