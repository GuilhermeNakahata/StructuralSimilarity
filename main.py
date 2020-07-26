from skimage.measure import compare_ssim
import cv2

# https://ourcodeworld.com/articles/read/991/how-to-calculate-the-structural-similarity-index-ssim-between-two-images-with-python

print("Iniciando Verificacao")
for i in range(1,101):
    for j in range (i+1,101):
        imageA = cv2.imread('Kengai/img_' + str(i) + '.jpg')
        imageB = cv2.imread('Kengai/img_' + str(j) + '.jpg')
        grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        (score, diff) = compare_ssim(grayA, grayB, full=True)
        diff = (diff * 255).astype("uint8")
        if(score > 0.7):
            print("Imagens possivelmente iguais: " + str(i) + " com a imagem: " + str(j))
            print("SSIM: {}".format(score))
