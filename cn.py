# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
# Initialising the CNN
# classifier = Sequential()
# # Step 1 - Convolution
# classifier.add(Conv2D(32, (3, 3), input_shape = (50, 65, 3), activation = 'relu'))
# # Step 2 - Pooling
# classifier.add(MaxPooling2D(pool_size = (2, 2)))
# # Adding a second convolutional layer
# classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
# classifier.add(MaxPooling2D(pool_size = (2, 2)))
# # Step 3 - Flattening
# classifier.add(Flatten())
# # Step 4 - Full connection
# classifier.add(Dense(units = 3, activation = 'softmax'))
# # classifier.add(Dense(units = 1, activation = 'softmax'))
# # Compiling the CNN
# classifier.compile(optimizer = 'adam', loss = 'sparse_categorical_crossentropy', metrics = ['accuracy'])
# # Part 2 - Fitting the CNN to the images
# from keras.preprocessing.image import ImageDataGenerator
# train_datagen = ImageDataGenerator(rescale = 1./255,
# shear_range = 0.2,
# zoom_range = 0.2,
# horizontal_flip = True)
# test_datagen = ImageDataGenerator(rescale = 1./255)
# training_set = train_datagen.flow_from_directory('train_data',
# target_size = (50, 65),
# batch_size = 10,
# class_mode = 'sparse')
# test_set = test_datagen.flow_from_directory('test_data',
# target_size = (50, 65),
# batch_size = 10,
# class_mode = 'sparse')

# print(len(training_set[0]))
# print(training_set[0][1].shape)

# classifier.fit_generator(training_set,
# steps_per_epoch = 800,
# epochs = 5,
# validation_data = test_set,
# validation_steps = 20)
# Part 3 - Making new predictions

# classifier.save('store')

classifier = keras.models.load_model('store')

import numpy as np
from keras.preprocessing import image
test_image = image.load_img('single_prediction/228_4.png', target_size = (50, 65))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)

# file = open('class_indices.txt','w')
# file.write(str(training_set.class_indices))
# print(training_set.class_indices)


print(result)
# print(result)
# if result[0][0] == 0:
#     prediction = 'A'
# else:
#     prediction = 'B'

# print(prediction)