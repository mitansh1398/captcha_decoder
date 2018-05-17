import urllib.request
from os.path import basename
import os
from PIL import Image
import keras
import pickle
from keras.preprocessing import image
import numpy as np


i = 1000
urllib.request.urlretrieve("https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq="+str(i), "predictions.png")
file = "predictions.png"
print("processing file %s"%(file))
filename = file
img = Image.open(filename)
print(img.size)
letter_1 = img.crop((0, 0, 50, 65))
letter_2 = img.crop((50, 0, 100, 65))
letter_3 = img.crop((100, 0,150, 65))
letter_4 = img.crop((150, 0, 200, 65))
letter_5 = img.crop((200, 0, 250, 65))

# print(basename(filename).split('.')[0])

letter_1.save("single_prediction/1.png")
letter_2.save("single_prediction/2.png")
letter_3.save("single_prediction/3.png")
letter_4.save("single_prediction/4.png")
letter_5.save("single_prediction/5.png")

classifier = keras.models.load_model('store')

pickle_in = open("dict.pickle","rb")
label = pickle.load(pickle_in)

ans=""

for i in range(1,6):
	print("running "+str(i))
	test_image = image.load_img('single_prediction/'+str(i)+".png", target_size = (50, 65))
	test_image = image.img_to_array(test_image)
	test_image = np.expand_dims(test_image, axis = 0)
	result = classifier.predict(test_image)	

	# print(result)
	y = result>0.9
	y = y[0]
	for index,i in enumerate(y):
		# print(i)
		if i == True:
			ans += str([l for l in label if label[l]==index][0])

print("labels : " + str(label))

print("prediction of image is : "+ans)
