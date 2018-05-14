import pickle
import numpy as np
import shutil
from keras.preprocessing import image
import keras
import os


classifier = keras.models.load_model('store')
pickle_in = open("dict.pickle","rb")
label = pickle.load(pickle_in)

directory = "output"
for file in os.listdir(directory):
	# file = input("enter the name of the file (with extension )")
	# file = "1_5.png"
	test_image = image.load_img('output/'+file, target_size = (50, 65))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)



	# print(result)
	y = result>0.9
	y = y[0]
	ans=""
	for index,i in enumerate(y):
		# print(i)
		if i == True:
			ans = str([l for l in label if label[l]==index][0])

	shutil.move("output/"+file, "new/"+ans+"/"+file)

	print("labels : " + str(label))

	print("prediction of image is : "+ans)
