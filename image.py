from os.path import basename

import os
from PIL import Image

directory = "images"
for file in os.listdir(directory):

    print("processing file %s"%(file))
    filename = file
    img = Image.open("images/"+filename)
    print(img.size)
    letter_1 = img.crop((0, 0, 50, 65))
    letter_2 = img.crop((50, 0, 100, 65))
    letter_3 = img.crop((100, 0,150, 65))
    letter_4 = img.crop((150, 0, 200, 65))
    letter_5 = img.crop((200, 0, 250, 65))

    # print(basename(filename).split('.')[0])

    letter_1.save("output/"+basename(filename).split('.')[0]+"_1.png")
    letter_2.save("output/"+basename(filename).split('.')[0]+"_2.png")
    letter_3.save("output/"+basename(filename).split('.')[0]+"_3.png")
    letter_4.save("output/"+basename(filename).split('.')[0]+"_4.png")
    letter_5.save("output/"+basename(filename).split('.')[0]+"_5.png")

