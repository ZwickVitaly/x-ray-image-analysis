from PIL import Image
import matplotlib as mpl
import numpy as np
import cv2


def pseudo_color_filter(src, cmap: str = "terrain"):
    cm_hot = mpl.cm.get_cmap(cmap)
    img_src = Image.open(src).convert('L')
    img_src.thumbnail((512, 512))
    im = np.array(img_src)
    im = cm_hot(im)
    im = np.uint8(im * 255)
    cv2.namedWindow("pseudo color", cv2.WINDOW_NORMAL)
    cv2.imshow('pseudo color', im)
    while True:
        k = cv2.waitKey(1)
        if cv2.getWindowProperty('pseudo color', cv2.WND_PROP_VISIBLE) <= 0:
            cv2.destroyAllWindows()
            break
        elif k == 27:
            print('ESC')
            cv2.destroyAllWindows()
            break
    # image = Image.fromarray(im)
    # return image
