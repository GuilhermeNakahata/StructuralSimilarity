import cv2
import numpy as np
import matplotlib.pyplot as plt

# https://ourcodeworld.com/articles/read/991/how-to-calculate-the-structural-similarity-index-ssim-between-two-images-with-python

print("Iniciando Verificacao")
for i in range(1,6):
    for j in range (i+1,6):
        print('Kengai/img_' + str(i) + '.jpg')
        print('Kengai/img_' + str(j) + '.jpg')
        imageA = cv2.imread('Kengai/img_' + str(i) + '.jpg')
        imageB = cv2.imread('Kengai/img_' + str(j) + '.jpg')
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        print(err)
        fig, ax = plt.subplots(1,3, figsize=(15, 15), squeeze=False)
        ax[0][0].imshow(imageA)
        ax[0][1].imshow(imageB)
        ax[0][2].imshow(imageB)
        plt.show()

