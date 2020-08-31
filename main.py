import cv2
import numpy as np
import matplotlib.pyplot as plt

from skimage.measure import compare_ssim

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
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        fig, ax = plt.subplots(1,2, figsize=(15, 15), squeeze=False)
        print(err)
        print(score)
        fig.suptitle("MSE: {:.2f}".format(err) + " SSIM: {:.2f}".format(score), fontsize=14)
        ax[0][0].imshow(imageA)
        ax[0][1].imshow(imageB)
        plt.show()

