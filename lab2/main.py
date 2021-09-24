import methods as met

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('plain.txt','r', encoding='utf-8')
    mensaje=str(file.read())
    mensaje=met.removeTildes(mensaje)
    mensaje=met.toUpper(mensaje)
    mensaje=met.removeSignos(mensaje)
    myKey="POSITIVO"
    traducido=Vignere_cipher(mensaje,myKey)
    print(traducido)
    traducido=Vignere_decipher(traducido,myKey)
    print(traducido)

def Vignere_cipher(message,key):
    i=0
    mssg_cipher=[]
    for caracter in message:
        k=key[i]
        num=LETRAS.find(caracter)
        num2=LETRAS.find(k)
        #print(num,num2)
        newnum=(num+num2)%len(LETRAS)
        mssg_cipher.append(LETRAS[newnum])
        if i==len(key)-1: i=0
        else : i+=1
    return ''.join(mssg_cipher)

def Vignere_decipher(message,key):
    i=0
    mssg_cipher=[]
    for caracter in message:
        k=key[i]
        num=LETRAS.find(caracter)
        num2=LETRAS.find(k)
        #print(num,num2)
        newnum=(num-num2)%len(LETRAS)
        mssg_cipher.append(LETRAS[newnum])
        if i==len(key)-1: i=0
        else : i+=1
    return ''.join(mssg_cipher)

if __name__ == '__main__':
    main()
