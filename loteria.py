#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install pandas
pip install openpyxl


# In[1]:


import pandas as pd
import numpy as np
import openpyxl as openpy
datosLot = pd.read_excel("datos.xlsx", sheet_name='datos', header=None)
listaD=datosLot[0].values.tolist()

matriz=np.zeros((1000,1000))

cont=np.zeros(1000)
pos=0

#Cambios de estado y ocurrencias de un número
for i in range(len(listaD)):
    if(i!=0):
        matriz[pos][int(listaD[i])]+=1

    cont[(listaD[i])]+=1
    pos=int(listaD[i])

#Calcular la probabilidad
for i in range(1000):
    if cont[i]!=0:
        matriz[i]=matriz[i]/cont[i]

mInversa=np.zeros((1000,1000))

for i in range(1000):
    for j in range(1000):
        mInversa[i][j]= matriz[j][i]


# In[2]:


def calcularProbNum(numJugar,dia):
    condiInicial=np.zeros(1000)
    condiInicial[listaD[len(listaD)-1]]=1

    for i in range(dia):
        vectorPn=calcularSigNumero(condiInicial)
        condiInicial=vectorPn

    (pos, prob)=buscarMayorProbabilidad(vectorPn)
    print("La probabilidad de que caiga: ",numJugar, " dentro de ", dia, " es: ", vectorPn[numJugar], " alejado: ",
          prob-vectorPn[numJugar], " la cual es: ", prob, " con el número: ", pos)
    print("")
    print("")

def calcularNumEnxTiempo(dia):
    condiInicial=np.zeros(1000)
    condiInicial[listaD[len(listaD)-1]]=1

    for i in range(dia):
        vectorPn=calcularSigNumero(condiInicial)
        condiInicial=vectorPn

    (pos, prob)=buscarMayorProbabilidad(vectorPn)
    print("El número con mayor probabilidad de caer dentro de ",dia ," día(s) es: ", pos ," con probabilidad: ", prob)
    print("")
    print("")

def calcularSigNumero(condiInicial):
    vectProb=np.zeros(1000)

    for i in range(1000):
        for j in range(1000):
            vectProb[i]+=mInversa[i][j]*condiInicial[j]

    return vectProb


def buscarMayorProbabilidad(vector):
    mayor=vector[0]
    pos=0
    suma=0
    for i in range(len(vector)):
        suma+=vector[i]
        if vector[i]>mayor:
            mayor=vector[i]
            pos=i
    return (pos,mayor)

def predecirSigNum():
    dias=input("Número de dias: ")
    calcularNumEnxTiempo(int(dias))

def probabilidadCaigaNum():
    numAJugar=input("Número que quiere jugar: ")
    sema=input("Número de semanas: ")
    calcularProbNum(int(numAJugar), int(sema))

def predecirLoteria():
    op=0

    while op!=9:
        print("SI QUIERE OBTENER EL NÚMERO MÁS PROBABLE EN DETERMINADAS SEMANAS DIGITE EL '0' ")
        print("SI QUIERE OBTENER LA PROBABILIDAD DE QUE UN DETERMINADO NÚMERO CAIGA EN DETERMINADAS SEMANAS DIGITE EL '1' ")
        print("SI QUIERE SALIR DIGITE EL 9")
        op=int(input())
        if op==0:
            predecirSigNum()
        elif op==1:
            probabilidadCaigaNum()
        elif op!=9:
            print("OPCIÓN INCORRECTA")

    print("TERMINANDO.....")

predecirLoteria()


# In[ ]:




