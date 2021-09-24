def toUpper(text):
    acentos = ['á', 'é', 'í', 'ó', 'ú']
    for caracter in text:
        if 'a'<=caracter<='z' or caracter in acentos:
            text = text.replace(caracter, caracter.upper())
    return text

def removeTildes(text):
    acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
    for acen in acentos:
        if acen in text:
            text = text.replace(acen, acentos[acen])
    return text

def removeSignos(text):
    symbols=['.', '!', '¡', ';', ',', ' ', '\n']
    for caracter in text:
        if caracter in symbols:
            text = text.replace(caracter, '')
    return text

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