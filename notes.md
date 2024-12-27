## Packages used
1. Pillow
2. OpenCV
3. PyTesseract


[Tesseract](https://medium.com/quantrium-tech/installing-and-using-tesseract-4-on-windows-10-4f7930313f82)


## Blogs
[Text Detection and Extraction using OpenCV and OCR](https://www.geeksforgeeks.org/text-detection-and-extraction-using-opencv-and-ocr)

# Steps of preprocessing

## Thresholding
- Thresholding is a technique in OpenCV, which is the assignment of pixel values in relation to the threshold value provided. In thresholding, each pixel value is compared with the threshold value. If the pixel value is smaller than the threshold, it is set to 0, otherwise, it is set to a maximum value (generally 255)
- Thresholding can only be achieved on grayscaled images, so it is important to convert the image into grayscale.
- Convert the image to grayscale. To do this we can use opencv pacakge 
  `cv2.cvtColor(image, flag)`. Possible values for flag are - 
  cv2.COLOR_BGR2GRAY and cv2.COLOR_BGR2HSV
- cv2.COLOR_BGR2GRAY helps us to convert an RGB image to gray scale image and cv2.COLOR_BGR2HSV is used to convert an RGB image to HSV (Hue, Saturation, Value) color-space image.
- Here we should use cv2.COLOR_BGR2GRAY. Once this step is done we apply threshold to image using cv2.threshold function

There are 3 types of thresholding: 
1. [Simple Thresholding](https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-1-simple-thresholding/)
2. [Adaptive Thresholding](https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-2-adaptive-thresholding/)
3. [Otsu’s Binarization](https://www.geeksforgeeks.org/python-thresholding-techniques-using-opencv-set-3-otsu-thresholding/)

