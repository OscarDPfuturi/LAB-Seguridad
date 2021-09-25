import methods as met

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('plain.txt','r', encoding='utf-8')
    mensaje=str(file.read())
    mensaje=met.removeSignos(mensaje)
    mensaje=met.removeTildes(mensaje)
    mensaje=met.toUpper(mensaje)
    myKey="LUNA"
    traducido=autoclave(mensaje,myKey,True)
    print(traducido)

def autoclave(message,key,action):
    i=0
    j=0
    mssg_cipher=[]
    d=1
    if action==False:
        d=-1
    for caracter in message:
        num=LETRAS.find(caracter)
        if i<len(key):
            k=key[i]
            num2=LETRAS.find(k)*d
            i+=1
        else :
            num2=LETRAS.find(message[j])*d
            j+=1
        newnum=(num+num2)%len(LETRAS)
        mssg_cipher.append(LETRAS[newnum])
    return ''.join(mssg_cipher)

if __name__ == '__main__':
    main()
