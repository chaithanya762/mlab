import tensorflow as tf
from tensorflow.keras.applications.vgg16 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np

model = tf.keras.applications.VGG16(weights='imagenet')

img_path = 'book.jpg'
img = image.load_img(img_path,target_size = (224,224))
x = image.img_to_array(img)
x = np.expand_dims(x,axis=0)
x = preprocess_input(x)

preds = model.predict(x)
decoded_preds = decode_predictions(preds,top=10)[0]

for _,label,prob in decoded_preds:
    print(f"{label}: {prob*100:.2f}%")
