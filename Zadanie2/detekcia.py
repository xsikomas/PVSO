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
stop = False
while stop == False:

    cam.get_image(img)
    image = img.get_image_data_numpy()
    image = cv2.resize(image, (480, 480))
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    gray = cv.medianBlur(gray, 5)
    rows = gray.shape[0]
    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows / 8, param1=29, param2=68, minRadius=0, maxRadius=0)
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv.circle(image, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv.circle(image, center, radius, (255, 0, 255), 3)
    cv.imshow("detected circles", image)
    cv.waitKey(2)




    if cv2.waitKey(33) == ord('a'):
       stop = True



#stop data acquisition
print('Stopping acquisition...')
cam.stop_acquisition()

#stop communication
cam.close_device()

print('Done.')