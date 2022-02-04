import cv2
import numpy as np


def resizeImg(img, w):
    dim = None
    imgH, imgW = img.shape[:2]

    if w == None:
        return (imgW, imgH)
    else:
        r = w/float(imgW)
        dim = (w, int(imgH * r * 0.55))
    return dim


def main():
    imgO = "bath.jpeg"

    #read img from file and convert to gray scale
    src = cv2.imread(imgO)
    imgG = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    #since img will be shown in terminal reduce aspect ratio of image
    imgR = cv2.resize(imgG, resizeImg(imgG, w = 200))

    #convert 0-255 value into ascii character
    chars = ['$', '8', '#', 'h', 'p', 'v', 'o', 'r', '~', ':', '_', '.']
    newImg = [[chars[pixel//22] for pixel in row] for row in imgR]
    for l in newImg:
        print("".join(l), end = "\n")

if __name__ == '__main__':
    main()


