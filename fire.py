import numpy as np
import tensorflow as tf
import tensorflow.keras.backend as K
import cv2
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing import image
import warnings

warnings.filterwarnings("ignore")

model = tf.keras.models.load_model('modelfire.h5')

def check_area(image):
  frame = image
  frame = cv2.resize(frame, (500, 500))
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
  hl = 0
  sl = 0
  vl = 246
  hh = 255
  sh = 255
  vh = 255

  low = np.array([hl, sl, vl])
  high = np.array([hh, sh, vh])

  mask = cv2.inRange(hsv, low, high)

  _, thresh = cv2.threshold(mask, 125, 255, cv2.THRESH_BINARY)
  contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
  totalArea = 0
  for i in range(0, len(contours)):
      approx = cv2.approxPolyDP(contours[i], 0.01 * cv2.arcLength(contours[i], True), True)
      area = cv2.contourArea(contours[i])
      totalArea = totalArea + area
      cv2.drawContours(frame, contours, i, (0, 255, 0), 2)

  #cv2_imshow( mask)
  #cv2_imshow(frame)
  t = 1
  return (totalArea/2500)


def cost_calc(arr, image):
  cost=0
  if arr == 0:
    cost = check_area(image)
  return cost


def fire(filename):
  file = cv2.imread(filename)

  image_path = filename
  img = load_img(image_path, target_size = (224, 224))
  x = image.img_to_array(img)
  x = np.expand_dims(x, axis=0)
  x = x/255
  p = model.predict(x)
  
  return cost_calc(np.argmax(p), file)
