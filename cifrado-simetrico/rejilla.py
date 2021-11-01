import methods as met

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    #name
    file = open('mensaje.txt','r',encoding='utf-8')
    mssg = file.read()
    file.close()
    #splittingMessage(mssg)
    rejilla = [[0, 0],[0, 2],[1, 4],[2, 1],[2, 3],[3, 1],[4, 5],[5, 2],[5, 4]]
    mssg = met.removeSpaces(mssg)
    cryptoGrid(mssg, rejilla)
    rotate(rejilla)

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

def cryptoGrid(mssg, rejilla):
    text = splittingMessage(mssg)
    ciphertext = []
    
    for i in range(1):
        textn = text[i]
        print(textn)
        for k in range(4):
            for j in range(len(rejilla)):
                ciphertext.append(textn[rejilla[j][0]][rejilla[j][1]])
            rejilla = sorted(rotate(rejilla))
    ciphertext = ''.join(ciphertext)
    print(ciphertext)
    

if __name__ == '__main__' :
    main()