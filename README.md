# Captcha Decoder
It is always boring to enter the captchas !!
This is a Image Classifier model using Convolutional Neural Network using “[keras](https://keras.io/)”


----------
## **Dependencies** :
- [keras](https://keras.io/)
- [tensorflow>=1.8](https://www.tensorflow.org/install/)
- [pandas](https://pandas.pydata.org/pandas-docs/stable/install.html)
- [python>=3.5](https://www.python.org/downloads/)


----------
## **Usage** :

**Creating the model** 


> Optional : Although the Directory contains pre-trained model file , run the following command to recreate the model . 
> Creating model takes time !!!


    python create_model.py

Now we will generate the test data and classify it 


    python3 generate_test_data.py
    python3 classify_test_data.py


> This will generate the test data from raw images in the images folder and classify and fill the predictions folder


----------


## **Model Summary :**
![Model Summary](https://d2mxuefqeaa7sj.cloudfront.net/s_33937C6A55F95E62EB36CF09C88A4C6343500DC1428A858E8AA303E053C2D218_1526580115301_summary.png)



----------


