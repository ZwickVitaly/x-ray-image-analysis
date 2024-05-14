import cv2
import numpy as np
import matplotlib.pyplot as plt


def hist_3d(src):
    imbgr = cv2.imread(src)
    imlab = cv2.cvtColor(imbgr, cv2.COLOR_BGR2LAB)
    plt.figure("3d histogram")
    ax = plt.axes(projection="3d")
    y = range(imlab.shape[0])
    x = range(imlab.shape[1])
    X, Y = np.meshgrid(x, y)
    ax.plot_surface(X, Y, imlab[:, :, 0], cmap=plt.cm.gray)
    plt.show()
