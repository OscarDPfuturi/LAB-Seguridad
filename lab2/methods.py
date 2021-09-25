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
    abc=[0]*27
    for caracter in text:
        orden=ord(caracter)
        if 64<orden<91:
            abc[orden-65]+=1
        elif 96<orden<123:
            abc[orden-97]+=1
        elif orden==209: #Ñ
            abc[26]+=1

    for i in range(26):
        if i==14:
            print('Ñ:',abc[26])
        print(chr(65+i)+':', abc[i])
