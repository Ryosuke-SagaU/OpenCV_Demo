import cv2
import numpy as np

# 画像の読み込み パスをどこに設定する?
# エスケープシーケンス(/n 改行などを表す)と判断されるので、これを無効化させる。
# / → // で表現する
img = cv2.imread("C:\\Users\\Ryosuke Nikushi\\picture.png")

# GrayPicture
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ここに，パスを通して保存する
cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img_gray)