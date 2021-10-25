import numpy as np
import os
import random
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import keras.backend as K

from tensorflow.keras.layers import Flatten, Dense, Dropout
from tensorflow.keras.callbacks import ReduceLROnPlateau, ModelCheckpoint, LearningRateScheduler
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.applications import MobileNetV2

import cv2
import matplotlib.pyplot as plt

print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

train_dir = '/content/drive/MyDrive/Fire-Safety-Dataset/Train/'
train_datagen = ImageDataGenerator(rescale=1./255,
    shear_range=0.1,
    zoom_range=0.1,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
    vertical_flip=True,
    validation_split=0.1
                                  )
train_generator = train_datagen.flow_from_directory(train_dir,
                                                    batch_size=16,
                                                    class_mode='categorical',
                                                    target_size=(224,224),
                                                    subset = 'training',
                                                    shuffle = True)

validation_dir = train_dir
validation_datagen = ImageDataGenerator(rescale=1.0/255,
                                        validation_split = 0.1
                                        )
validation_generator = validation_datagen.flow_from_directory(validation_dir,
                                                              batch_size=16,
                                                              subset = 'validation',
                                                              class_mode ='categorical',
                                                              target_size=(224,224),
                                                              shuffle = True)

test_dir = '/content/drive/MyDrive/Fire-Safety-Dataset/Test/'
test_datagen = ImageDataGenerator(rescale = 1./255,
                                  )
test_generator =test_datagen.flow_from_directory(test_dir,
                                                batch_size=16,
                                                class_mode ='categorical',
                                                target_size=(224,224),
                                                shuffle = True)

base_model = MobileNetV2(
    include_top=False, weights='imagenet', input_tensor=None,
    input_shape=(224,224,3), classes = 2
)

fine_tune_at = int (len(base_model.layers)*0.7)
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable =  False

model = tf.keras.models.Sequential()
model.add(base_model)
model.add(Flatten())
model.add(Dense(128,activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(64,activation='relu'))
model.add(Dense(2,activation='softmax'))
# load weights 
model.compile(optimizer = Adam(lr=2e-5), loss='binary_crossentropy', metrics=['acc'])
model.summary()


filepath= 'modelfire.h5'  
my_callbacks = [
  ReduceLROnPlateau(
    monitor='val_acc', factor=0.5, patience=3, verbose=True,
    mode='auto', min_delta=0.000001, cooldown=0, min_lr=0 
  ), 
  ModelCheckpoint(
    filepath, monitor='val_loss', verbose=0, save_best_only=True, mode= 'min')]


history = model.fit(train_generator,
                    shuffle = True,
                    epochs=10,
                    workers = 8,
                    verbose=True,
                    validation_data=validation_generator,
                    callbacks=my_callbacks)


acc = history.history['acc']
val_acc = history.history['val_acc']

loss = history.history['loss']
val_loss = history.history['val_loss']

print(acc)
print(val_acc)

plt.figure(figsize=(8, 8))
plt.subplot(2, 1, 1)
plt.plot(acc, label='Training Accuracy')
plt.plot(val_acc, label='Validation Accuracy')
plt.legend(loc='lower right')
plt.ylabel('Accuracy')
plt.ylim([min(plt.ylim()),1])
plt.title('Training and Validation Accuracy')

plt.subplot(2, 1, 2)
plt.plot(loss, label='Training Loss')
plt.plot(val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.ylabel('Cross Entropy')
plt.ylim([0,max(plt.ylim())])
plt.title('Training and Validation Loss')
plt.show()
