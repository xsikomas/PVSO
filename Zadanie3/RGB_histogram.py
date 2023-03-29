import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2 as cv


# function to obtain histogram of an image
def hist_plot(img):
    # empty list to store the count
    # of each intensity value
    count = []

    # empty list to store intensity
    # value
    r = []

    # loop to traverse each intensity
    # value
    for k in range(0, 256):
        r.append(k)
        count1 = 0

        # loops to traverse each pixel in
        # the image
        for i in range(m*n):
            if img[i] == k:
                count1 += 1
        count.append(count1)

    return (r, count)


img = Image.open('2.jpg')

pixels = list(img.getdata())

# To ascertain total numbers of rows and
# columns of the image, size of the image

# m, n = img.shape
m=240
n=240


img_red = np.delete(pixels, [0, 1], 1)
img_green = np.delete(pixels, [0, 2], 1)
img_blue = np.delete(pixels, [1, 2], 1)

r_red, count_red = hist_plot(img_red)
r_green, count_green = hist_plot(img_green)
r_blue, count_blue = hist_plot(img_blue)

plt.plot(r_red, count_red, "r-", label="red")
plt.plot(r_green, count_green, "g-", label="green")
plt.plot(r_blue, count_blue, "b-", label="blue")
plt.legend(loc="upper right")
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the all channels')
plt.savefig("mygraph.jpg")
plt.close()

plt.plot(r_red, count_red, "r-", label="red")
plt.legend(loc="upper right")
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the red channel')
plt.savefig("redchannel.jpg")
plt.close()

plt.plot(r_green, count_green, "g-", label="green")
plt.legend(loc="upper right")
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the green channel')
plt.savefig("greenchannel.jpg")
plt.close()

plt.plot(r_blue, count_blue, "b-", label="blue")
plt.legend(loc="upper right")
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the blue channel')
plt.savefig("bluechannel.jpg")

image1 = cv2.imread("bluechannel.jpg")
image2 = cv2.imread("redchannel.jpg")
image3 = cv2.imread("greenchannel.jpg")
image4 = cv2.imread("mygraph.jpg")

Horizontal1 = np.hstack([image1, image2])
Horizontal2 = np.hstack([image3, image4])
Vertical_attachment = np.vstack([Horizontal1, Horizontal2])

cv2.imwrite("all4" + ".jpg", Vertical_attachment)




