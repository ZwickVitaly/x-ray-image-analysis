import cv2
from PIL import Image
import numpy as np


def sobel_filter(src):
    d_dept = cv2.CV_16S
    if not isinstance(src, str):
        image_pil = Image.open(src)
        img_src = np.asarray(image_pil)
    else:
        img_src = cv2.imread(src)

    gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
    x = cv2.Sobel(gray, d_dept, 1,0, ksize=3, scale=1)
    y = cv2.Sobel(gray, d_dept, 0,1, ksize=3, scale=1)
    absx= cv2.convertScaleAbs(x)
    absy = cv2.convertScaleAbs(y)
    edge = cv2.addWeighted(absx, 0.5, absy, 0.5, 0)
    cv2.namedWindow("sobel", cv2.WINDOW_NORMAL)
    cv2.imshow('sobel', edge)
    while True:
        k = cv2.waitKey(1)
        if cv2.getWindowProperty('sobel', cv2.WND_PROP_VISIBLE) <= 0:
            cv2.destroyAllWindows()
            break
        elif k == 27:
            print('ESC')
            cv2.destroyAllWindows()
            break
