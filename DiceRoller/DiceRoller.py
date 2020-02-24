# -*- coding: utf-8 -*-

import random

def cls():
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 

def RollD10(Qnt,Dif):
    import random
    Sucessos=0
    SucessoAnulado=0
    Jogada=[]
    for i in range(Qnt):
        result=(random.randint(1,10))
        Jogada.append(result)
        if result==10:
            Sucessos+=1
            #RolarD10(1,Dif)
        elif result>=Dif:
            Sucessos+=1
        elif result==1: #resultado 1 anula um sucesso
             Sucessos-=1
             SucessoAnulado+=1
        
    print(Jogada)
    print("Número de sucessos: "+str(Sucessos)+". (Anulados:"+str(SucessoAnulado)+")")
        
Repetir=True
while Repetir==True:
    cls()
    QntDados=int(input("Quantos D10 serão rolados? "))
    Dificuldade=int(input("Qual a dificuldade? "))
    
    if QntDados<1 or Dificuldade<1 or Dificuldade>10:
        print("\nDados inválidos, não é possível fazer a rolagem.")
    else:
        RolarD10(QntDados, Dificuldade)
    
    Repetir=input("\nRepetir? s/n ")
    if Repetir=="s":
        Repetir=True
    elif Repetir=="n":
        Repetir=False
    else:
        print("\nResposta Inválida! Programa encerrado.\n")
        Repetir=False