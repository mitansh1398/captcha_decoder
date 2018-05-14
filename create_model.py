# Importing the Keras libraries and packages
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
import pickle
# Initialising the CNN
classifier = Sequential()
# Step 1 - Convolution
classifier.add(Conv2D(32, (3, 3), input_shape = (50, 65, 3), activation = 'relu'))
# Step 2 - Pooling
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Adding a second convolutional layer

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))
# Step 3 - Flattening
classifier.add(Flatten())

# classifier.add(Dense(units = 200, activation = 'relu'))
# classifier.add(Dense(units = 100, activation = 'relu'))
# classifier.add(Dense(units = 128, activation = 'relu'))

# Step 4 - Full connection
classifier.add(Dense(units = 120,activation='relu'))

classifier.add(Dense(units = 28, activation = 'softmax'))
# classifier.add(Dense(units = 1, activation = 'softmax'))
# Compiling the CNN
classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])
# Part 2 - Fitting the CNN to the images
from keras.preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(rescale = 1./255,
shear_range = 0.2,
zoom_range = 0.2,
horizontal_flip = True)
test_datagen = ImageDataGenerator(rescale = 1./255)
training_set = train_datagen.flow_from_directory('train_data',
target_size = (50, 65),
batch_size = 32,
class_mode = 'categorical')
test_set = test_datagen.flow_from_directory('test_data',
target_size = (50, 65),
batch_size = 32,
class_mode = 'categorical')

print(classifier.summary())

classifier.fit_generator(training_set,
steps_per_epoch = 200,
epochs = 20,
validation_data = test_set,
validation_steps = 20)
# Part 3 - Making new predictions

classifier.save('store')

pickle_out = open("dict.pickle","wb")
pickle.dump(training_set.class_indices, pickle_out)
pickle_out.close()

file = open('class_indices.txt','w')
file.write(str(training_set.class_indices))
file.close()


