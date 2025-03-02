import tensorflow as tf
import numpy as np
import cv2
import sys

# Load the trained model (Ensure the path is correct)
model = tf.keras.models.load_model("saved_model/brain_tumor_vgg16_final.keras", compile=False)

# Class labels
class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

def predict_brain_tumor(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            print(f" Error: Could not read image at {image_path}. Check the path and try again.")
            return
        
        # Preprocess the image
        image = cv2.resize(image, (224, 224))  # Resize to match model input size
        image = np.array(image) / 255.0  # Normalize pixel values
        image = np.expand_dims(image, axis=0)  # Add batch dimension

        # Make prediction
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction)*100

        # Determine if the user has a tumor
        if class_names[predicted_class] == "No Tumor":
            result = " No Brain Tumor Detected!"
        else:
            result = f"Tumor Detected: {class_names[predicted_class]}"

        # Display results
        print(result)
        print(f"Confidence: {confidence:.2f} %")

    except Exception as e:
        print(f"Error processing image: {e}")

if __name__ == "__main__":
    # Default test image path
    image_path = "C:/Users/user/Desktop/brain_tumor_project/dataset/test/glioma/Te-gl_0010.jpg"

    # Use provided image path from command line
    if len(sys.argv) > 1:
        image_path = sys.argv[1]  # Fix: Use sys.argv[1] instead of sys.argv[2]

    predict_brain_tumor(image_path)
