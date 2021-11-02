import methods as met
import numpy as np
LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('mensaje.txt','r',encoding='utf-8')
    mssg = file.read()
    file.close()
    rejilla = [[0, 0],[0, 2],[1, 4],[2, 1],[2, 3],[3, 1],[4, 5],[5, 2],[5, 4]]
    mssg = met.removeSpaces(mssg)
    encrypt(mssg, rejilla)

    file = open('cifrado.txt','r',encoding='utf-8')
    enc_mssg = file.read()
    file.close()
    print("Mensaje descifrado:")
    decipher(enc_mssg, rejilla)

def splittingMessage(mssg):
    mssg_len = len(mssg)
    text = []
    i = 0
    while i < mssg_len:
        mat = []
        for j in range(6):
            row = []
            for k in range(6):
                if i + (j * 6) + k < mssg_len:
                    row.append(mssg[i+(j*6)+k])
                else :
                    row.append('X')
            mat.append(row)
        text.append(mat)
        i+=36
    return text

def rotate(rejilla):
    new_rejilla = []
    for i in range(len(rejilla)):
        row = rejilla[i][1]
        col = 6 - 1 - rejilla[i][0]
        new_rejilla.append([row, col])
    return new_rejilla

def printMat(mssg):
    print("Mensaje dividido:")
    for i in range(len(mssg)):
        print(mssg[i])

def encrypt(mssg, rejilla):
    text = splittingMessage(mssg)
    ciphertext = []
    
    for i in range(1):
        textn = text[i]
        printMat(textn)
        for k in range(4):
            for j in range(len(rejilla)):
                ciphertext.append(textn[rejilla[j][0]][rejilla[j][1]])
            rejilla = sorted(rotate(rejilla))
    ciphertext = ''.join(ciphertext)
    print(ciphertext)
    
def decipher(enc_mssg, rejilla):
    mssg = [['X']*6]*6
    mssg = np.array(mssg)
    #enc_mssg = splittingMessage(enc_mssg)
    #print(mssg)
    rej_len = len(rejilla)
    #while k < len(enc_mssg):
    for i in range(4):
        for j in range(rej_len):
            #mssg[rejilla[j][0]][rejilla[j][1]] = enc_mssg[j+i*9]
            mssg[rejilla[j][0], rejilla[j][1]] = enc_mssg[j+i*9]
        #print(mssg[0])
        #print(mssg)
        rejilla = sorted(rotate(rejilla))
    #mssg[5][5] = 'X'
    print(mssg)

if __name__ == '__main__' :
    main()
