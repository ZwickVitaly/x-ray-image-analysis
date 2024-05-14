import numpy as np
import cv2
from PIL import Image


def high_pass_filter(src):
    if not isinstance(src, str):
        image_pil = Image.open(src)
        img_src = np.asarray(image_pil)
    else:
        img_src = cv2.imread(src)

    kernel = np.array([[0.0, -1.0, 0.0],
                       [-1.0, 4.1, -1.0],
                       [0.0, -1.0, 0.0]])

    kernel = kernel/(np.sum(kernel) if np.sum(kernel) != 0 else 1)

    img_rst = cv2.filter2D(img_src, -1, kernel)
    cv2.namedWindow("high_pass", cv2.WINDOW_NORMAL)
    cv2.imshow('high_pass', img_rst)
    while True:
        k = cv2.waitKey(1)
        if cv2.getWindowProperty('high_pass', cv2.WND_PROP_VISIBLE) <= 0:
            cv2.destroyAllWindows()
            break
        elif k == 27:
            print('ESC')
            cv2.destroyAllWindows()
            break
