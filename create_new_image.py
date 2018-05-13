import urllib.request
from os.path import basename
import os
from PIL import Image

i = 1000
urllib.request.urlretrieve("https://webmail.iitg.ernet.in/plugins/captcha/backends/watercap/image_generator.php?sq="+str(i), "new.png")
file = "new.png"
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


