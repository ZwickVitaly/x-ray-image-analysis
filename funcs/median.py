import cv2


def median_filter(src):
    img = cv2.imread(src)
    removed_noise = cv2.medianBlur(img, 3)
    cv2.namedWindow("median", cv2.WINDOW_NORMAL)
    cv2.imshow('median', removed_noise)
    while True:
        k = cv2.waitKey(1)
        if cv2.getWindowProperty('median', cv2.WND_PROP_VISIBLE) <= 0:
            cv2.destroyAllWindows()
            break
        elif k == 27:
            print('ESC')
            cv2.destroyAllWindows()
            break
