import tensorflow as tf
import numpy as np
import cv2
import sys

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"
#loading trained model by vgg16_brain_tumor.py 
model = tf.keras.models.load_model("saved_model/brain_tumor_vgg16_final.keras", compile=False)

class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

def predict_brain_tumor(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f" Error: Could not read image at {image_path}. Check the path and try again.")
            return
        
        # Preprocessing
        image = cv2.resize(image, (224, 224)) 
        image = np.array(image) / 255.0  # Normalizing pixel values
        image = np.expand_dims(image, axis=0)  

      
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)*100

        if class_names[predicted_class] == "No Tumor":
            result = " No Brain Tumor Detected!"
        else:
            result = f"Tumor Detected: {class_names[predicted_class]}"

        print(result)
        print(f"Confidence: {confidence:.2f} %")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":

    image_path = "" #"give local test image path"

    if len(sys.argv) > 1:
        image_path = sys.argv[1] 

    predict_brain_tumor(image_path)
