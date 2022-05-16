import cv2
import numpy as np

# 画像の読み込み パスをどこに設定する?
# エスケープシーケンス(/n 改行などを表す)と判断されるので、これを無効化させる。
# / → // で表現する
img = cv2.imread("C:\\Users\\Ryosuke Nikushi\\GrayPicture.png")

#y_step=50
#x_step=50
y_step=40
x_step=20

img_y,img_x=img.shape[:2]

img[y_step:img_y:y_step, :, :] = 255
img[:, x_step:img_x:x_step, :] = 255

cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img)

#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ここに，パスを通して保存する
#cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img_gray)