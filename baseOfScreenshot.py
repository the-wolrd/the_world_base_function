from PIL import ImageGrab
import numpy as np
import cv2

# the fastest speed
im = ImageGrab.grab(bbox=(0, 0, 1920, 1080))# bbox=(x(start), y(start), x(end), y(end)) The main img of screenshot
im = np.array(im) # convert np array
cv_img = im.astype(np.uint8) # match type(cv2.imread)
cv_gray = cv2.cvtColor(cv_img, cv2.COLOR_RGB2GRAY) # convert gray img before cv2.matchTemplate
template = cv2.imread('test.png', 0)
# call a template img and convert gray img ('test.png', this is convert gray img--->0)
res = cv2.matchTemplate(cv_gray,template,cv2.TM_CCOEFF_NORMED) # use matchTemplate (main img, compare img, i don't know)
threshold = 0.99 # confidence
loc = np.where(res >= threshold)
x_y = []
for xy in zip(*loc[::-1]): # search internet
    x_y.append(xy)
print(x_y)

def function(x1, y1, x2, y2, template_img):
    im = ImageGrab.grab(bbox=(x1, y1, x2, y2))
    im = np.array(im)
    cv_img = im.astype(np.uint8)
    cv_gray = cv2.cvtColor(cv_img, cv2.COLOR_RGB2GRAY)
    template = cv2.imread(template_img, 0)
    res = cv2.matchTemplate(cv_gray,template,cv2.TM_CCOEFF_NORMED)
    threshold = 0.99
    loc = np.where(res >= threshold)
    x_y = []
    for pt in zip(*loc[::-1]):
        x_y.append(pt)
    return x_y

pos_xy = function(0, 0, 1920, 1080, 'test.png')

# the original(very slower)
im = ImageGrab.grab(bbox=(0, 0, 1920, 1080))
im.save('test.png')
cv_img = cv2.imread('test.png')
cv_gray = cv2.cvtColor(cv_img, cv2.COLOR_RGB2GRAY)
template = cv2.imread('test.png', 0)
res = cv2.matchTemplate(cv_gray,template,cv2.TM_CCOEFF_NORMED) # use matchTemplate (main img, compare img, i don't know)
threshold = 0.99 # confidence
loc = np.where(res >= threshold)
x_y = []
for xy in zip(*loc[::-1]): #search internet
    x_y.append(xy)

print(x_y) # (x, y)