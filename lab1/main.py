# 1.
def substitution(text, file):
    subs = {'j': 'i', 'J': 'I', 'h': 'i', 'H': 'I', 'ñ': 'n', 'k': 'l', 'u': 'v', 'w': 'v', 'y': 'z', 'Y': 'Z'}
    for caracter in text:
        if caracter in subs:
            text = text.replace(caracter, subs[caracter])
    file.write(text)

# 2.
def removeTildes(text, file):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for acen in acentos:
        if acen in text:
            text = text.replace(acen, acentos[acen])
    file.write(text)

# 3.
def toUpper(text, file):
    acentos = ['á', 'é', 'í', 'ó', 'ú']
    for caracter in text:
        if 'a'<=caracter<='z' or caracter in acentos:
            text = text.replace(caracter, caracter.upper())
    file.write(text)

# 4.
def removeSignos(text, file):
    symbols=['.', '!', '¡', ';', ',', ' ', '\n']
    for caracter in text:
        if caracter in symbols:
            text = text.replace(caracter, '')
    file.write(text)

# 5.
def frecuencias(text):
    acentos = {'á': 0, 'é': 4, 'í': 8, 'ó': 14, 'ú': 20, 'Á': 0, 'É': 4, 'Í': 8, 'Ó': 14, 'Ú': 20}
    abc=[0]*26
    for caracter in text:
        orden=ord(caracter)
        if 64<orden<91:
            abc[orden-65]+=1
        elif 96<orden<123:
            abc[orden-97]+=1
        if orden in acentos:
            abc[acentos[caracter]]

    index=[]
    j = 0
    while len(index) < 5:
        m = 0
        i = 0
        while i < 26:
            if i not in index and m < abc[i]:
                m = abc[i]
                j = i
            i+=1
        index.append(j)
    print(index)

    for i in range(26):
        if i in index:
            print(chr(97+i)+': ', abc[i], '(', index.index(i)+1,')')
        else :
            print(chr(97+i)+': ', abc[i])

def kasiski(text):
    trigram = []
    for i in range(len(text)):
        trigram = text[i:i+3]
        d = 0
        for j in range(i,len(text)):
            if j != i and trigram == text[j:j+3] and ' ' not in trigram and '\n' not in trigram:
                print(trigram, d)
            d+=1

def unicode8(text):
    text = text.decode("utf-8", 'strict')
    print(text)

def aqui(text):
    text2 = []
    for i in range(len(text)):
        if i%20==0 and i!=0:
            text2.append('AQUÍ')
        else :
            text2.append(text[i])

    while len(text2)%4!=0:
        text2.append('X')
    text2 = ''.join(text2)
    print(text2)

def main():
    file = open('texto.txt','r',encoding='utf-8')
    text = file.read()
    file.close()

    file = open('HERALDOSNEGROS_pre.txt','w')
    substitution(text, file)
    #removeTildes(text, file)
    #toUpper(text, file);
    #removeSignos(text, file)
    #frecuencias(text)
    #kasiski(text)
    #unicode8(text)
    #aqui(text)
    file.close()

if __name__ == '__main__' :
    main()