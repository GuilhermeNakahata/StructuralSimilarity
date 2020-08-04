import glob
import os
import pandas as pd
from urllib.parse import urlparse

from skimage.measure import compare_ssim
import cv2

chokkan_pinterest = glob.glob(os.path.join('ShakanPinterest/', '*'))

chokkan_dir = glob.glob(os.path.join('Shakan/', '*'))

listaA = []

listaB = []

elementoInicial = 0

print("Iniciando Verificacao")
for i in chokkan_dir:
    for f in chokkan_pinterest:
        imageA = cv2.imread(i)
        imageB = cv2.imread(f)
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        if(score > 0.9):
            Valor = i.split("/")[1]
            Valor1 = Valor.split("_")[1]
            Valor2 = Valor1.split(".")[0]
            listaA.append(int(Valor2))
            listaB.append(f.split("/")[1])

listaNomeImg = []
listaUrl = []
listaUrlMatch = []

f = open('index.txt', 'r')

print("Abrindo o arquivo")

for line in f:
    listaUrl.append(line.split("\n")[0])
    url = urlparse(line).path.split("/")[5]
    url = url.split("\n")[0]
    listaNomeImg.append(url)

f.close()

achado = True

print("Verificando URLs")

for i in listaB:
    index = 0
    achado = False
    for j in listaNomeImg:
        index = index + 1
        if(i == j):
            listaUrlMatch.append(listaUrl[index-1])
            achado = True
            break

    if(achado == False):
        listaUrlMatch.append("Nao possui no arquivo index.txt")

obj = {'Name Image': listaA, 'url': listaUrlMatch}

df = pd.DataFrame(data=obj)

df_ordenado = df.sort_values(by='Name Image')

print(df_ordenado.to_string())

df_ordenado.to_excel("output.xlsx")