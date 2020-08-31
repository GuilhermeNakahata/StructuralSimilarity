import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage.measure import compare_ssim

# https://ourcodeworld.com/articles/read/991/how-to-calculate-the-structural-similarity-index-ssim-between-two-images-with-python
# https://www.pyimagesearch.com/2014/09/15/python-compare-two-images/

print("Iniciando Verificacao")
for i in range(1,101):
    for j in range (i+1,101):
        imageA = cv2.imread('Arruda/imagem' + str(i) + '.jpg')
        imageB = cv2.imread('Arruda/imagem' + str(j) + '.jpg')
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        if(err < 3000):
            print("Imagens possivelmente iguais: " + str(i) + " com a imagem: " + str(j))
            print("SSIM: {}".format(err))

