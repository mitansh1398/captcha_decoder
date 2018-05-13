import pickle
import numpy as np
from keras.preprocessing import image
import keras


classifier = keras.models.load_model('store')

file = input("enter the name of the file (with extension )")
test_image = image.load_img('single_prediction/'+file, target_size = (50, 65))
test_image = image.img_to_array(test_image)
test_image = np.expand_dims(test_image, axis = 0)
result = classifier.predict(test_image)

pickle_in = open("dict.pickle","rb")
label = pickle.load(pickle_in)

print(result)
y = result>0.9
y = y[0]
ans=""
for index,i in enumerate(y):
	# print(i)
	if i == True:
		ans = str([l for l in label if label[l]==index])

print("labels : " + str(label))

print("prediction of image is : "+ans)
