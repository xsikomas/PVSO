import cv2 as cv
from ximea import xiapi
import cv2
import sys
import numpy as np



### runn this command first echo 0|sudo tee /sys/module/usbcore/parameters/usbfs_memory_mb  ###
#create instance for first connected camera
cam = xiapi.Camera()



#start communication
#to open specific device, use:
#cam.open_device_by_SN('41305651')
#(open by serial number)
print('Opening first camera...')
cam.open_device()

# settings
cam.set_exposure(10000)
cam.set_param('imgdataformat','XI_RGB32')
cam.set_param('auto_wb', 1)
print('Exposure was set to %i us' %cam.get_exposure())

# create instance of Image to store image data and metadata
img = xiapi.Image()

# start data acquisition
print('Starting data acquisition...')
cam.start_acquisition()

x = 1
while cv2.waitKey() != ord('q') and x < 5:

    cam.get_image(img)
    image = img.get_image_data_numpy()
    image = cv2.resize(image, (240, 240))
    cv2.imshow("test", image)
    name = str(x)
    cv2.imwrite(name+".jpg", image)
    x = x+1

while cv2.waitKey() != ord('q'):
    image1 = cv2.imread("1.jpg")
    image2 = cv2.imread("2.jpg")
    image3 = cv2.imread("3.jpg")
    image4 = cv2.imread("4.jpg")

    Horizontal1 = np.hstack([image1, image2])
    Horizontal2 = np.hstack([image3, image4])
    Vertical_attachment = np.vstack([Horizontal1, Horizontal2])

    cv2.imwrite("4foto" + ".jpg", Vertical_attachment)

    cv2.imshow("First Collage", Vertical_attachment)
# kernel
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
    image_kernel = cv.filter2D(image1, -1, kernel)

# rotation
    image_rotate = np.zeros(shape=[240, 240, 3], dtype=np.uint8)
    for i in range(0, 240):
        for j in range(0, 240):
            image_rotate[j][239-i] = image2[i][j]

# RGB red channel
    image_red_channel = np.zeros(shape=[240, 240, 3], dtype=np.uint8)
    image_red_channel[:, :, 2] = image3[:, :, 2]

# Collage
    Hor1 = np.hstack([image_kernel, image_rotate])
    Hor2 = np.hstack([image_red_channel, image4])
    Collage = np.vstack([Hor1, Hor2])

    cv2.imshow("Final Collage", Collage)

    print("Shape: ", Collage.shape, "\n", "Size: ", Collage.size, "\n", "Data type: ", Collage.dtype)

# for i in range(10):
#     #get data and pass them from camera to img
#     cam.get_image(img)
#     image = img.get_image_data_numpy()
#     cv2.imshow("test", image)
#     cv2.waitKey()
#     #get raw data from camera
#     #for Python2.x function returns string
#     #for Python3.x function returns bytes
#     data_raw = img.get_image_data_raw()
#
#     #transform data to list
#     data = list(data_raw)
#
#     #print image data and metadata
#     print('Image number: ' + str(i))
#     print('Image width (pixels):  ' + str(img.width))
#     print('Image height (pixels): ' + str(img.height))
#     print('First 10 pixels: ' + str(data[:10]))
#     print('\n')

#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

print('Done.')