import cv2
import numpy as np

# 画像の読み込み パスをどこに設定する?
# エスケープシーケンス(/n 改行などを表す)と判断されるので、これを無効化させる。
# / → // で表現する
img = cv2.imread("C:\\Users\\Ryosuke Nikushi\\GrayPicture-80,360-20,200.png", 0)

ret2, img_otsu = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)

print("ret2: {}".format(ret2))

cv2.imshow("otsu", img_otsu)
cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img_otsu)
cv2.waitKey()
cv2.destroyAllWindows()

#y_step=50
#x_step=50
#y_step=40
#x_step=20

#img_y,img_x=img.shape[:2]

#img[y_step:img_y:y_step, :, :] = 255
#img[:, x_step:img_x:x_step, :] = 255

# [左がy座標,右がx座標]
#img1 = img[80 : 360, 20 : 200]
#cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img1)

#img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ここに，パスを通して保存する
#cv2.imwrite("C:\\Users\\Ryosuke Nikushi\\newpicture.png", img_gray)