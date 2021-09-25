import methods as met

LETRAS = ("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

def main():
    file = open('texto.txt','r', encoding='utf-8')
    mensaje=str(file.read())
    mensaje=met.removeTildes(mensaje)
    mensaje=met.toUpper(mensaje)
    mensaje=met.removeSignos(mensaje)
    myKey="POSITIVO"
    traducido=Vignere_cipher(mensaje,myKey,True)
    #print(traducido)
    met.frecuencias(traducido)

def Vignere_cipher(message,key,action):
    i=0
    mssg_cipher=[]
    d=1
    if action==False:
        d=-1
    for caracter in message:
        k=key[i]
        num=LETRAS.find(caracter)
        num2=LETRAS.find(k)*(d)
        #print(num,num2)
        newnum=(num+num2)%len(LETRAS)
        mssg_cipher.append(LETRAS[newnum])
        if i==len(key)-1: i=0
        else : i+=1
    return ''.join(mssg_cipher)

if __name__ == '__main__':
    main()
