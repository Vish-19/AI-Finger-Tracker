import cv2
import pandas as pd
img=cv2.imread('colorful_image.jpg')
clicked=False
csv = pd.read_csv('colors.csv', names=["color", "color_name", "hex", "R", "G", "B"], header=None)
def get_color_name(R, G, B):
    min=20000
    for i in range(len(csv)):
        d=abs(R - int(csv.loc[i, "R"])) + abs(G - int(csv.loc[i, "G"])) + abs(B - int(csv.loc[i, "B"]))
        if d<=min:
            min=d
            name=csv.loc[i, "color_name"]
    return name
def draw_function(event, x1, y1, flags, param):
    if event == cv2.EVENT_FLAG_LBUTTON:
        global b,g,r,x,y,clicked
        clicked = True
        x=x1
        y=y1
        b,g,r=img[y1,x1]
        b = int(b)
        g = int(g)
        r = int(r)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
while True:
    cv2.imshow("image", img)
    if clicked:
        cv2.rectangle(img, (20, 20), (450, 60), (b, g, r), -1)
        text = get_color_name(r, g, b)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2,cv2.FONT_HERSHEY_SCRIPT_SIMPLEX)
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.FONT_HERSHEY_SCRIPT_COMPLEX)
        clicked = False
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()