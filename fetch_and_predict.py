import urllib.request
from PIL import Image
import keras
import pickle
from keras.preprocessing import image
import numpy as np

#Fetching image for testing
urllib.request.urlretrieve(
    "https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq=" + str(1000),
    "predictions.png")
file = "predictions.png"
print("processing file %s" % (file))
filename = file

#Loading  test image
img = Image.open(filename)
print(img.size)
letter_1 = img.crop((0, 0, 50, 65))
letter_2 = img.crop((50, 0, 100, 65))
letter_3 = img.crop((100, 0, 150, 65))
letter_4 = img.crop((150, 0, 200, 65))
letter_5 = img.crop((200, 0, 250, 65))

#Saving cropped letters
letter_1.save("predictions/1.png")
letter_2.save("predictions/2.png")
letter_3.save("predictions/3.png")
letter_4.save("predictions/4.png")
letter_5.save("predictions/5.png")

#Loading Model
classifier = keras.models.load_model('store')

#Loading label dictionary from dict.pickle
pickle_in = open("dict.pickle", "rb")
label = pickle.load(pickle_in)

#Initialising ans variable
ans = ""

#Running Predicitons
for i in range(1, 6):
    print("running " + str(i))
    test_image = image.load_img('predictions/' + str(i) + ".png", target_size=(50, 65))
    test_image = image.img_to_array(test_image)
    test_image = np.expand_dims(test_image, axis=0)
    result = classifier.predict(test_image)

    #
    y = result > 0.9
    y = y[0]
    for index, i in enumerate(y):
        if i == True:
            ans += str([l for l in label if label[l] == index][0])

print("labels : " + str(label))

print("prediction of image is : " + ans)
