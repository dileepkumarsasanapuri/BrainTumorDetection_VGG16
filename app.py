import os
import tensorflow as tf
import numpy as np
import cv2
from flask import Flask, render_template, request

# Initialize Flask app
app = Flask(__name__)

# Ensure 'static/uploads' directory exists
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Load trained model
model = tf.keras.models.load_model("saved_model/brain_tumor_vgg16_final.keras", compile=False)

# Class labels
class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

def predict_brain_tumor(image_path):
    try:
        image = cv2.imread(image_path)
        if image is None:
            return None, "Error: Could not read image.", 0.0

        image = cv2.resize(image, (224, 224))
        image = np.array(image) / 255.0
        image = np.expand_dims(image, axis=0)

        prediction = model.predict(image)
        predicted_class = np.argmax(prediction)
        confidence = np.max(prediction) * 100

        tumor_status = "No Brain Tumor Detected!" if class_names[predicted_class] == "No Tumor" else f"⚠️ Tumor Detected: {class_names[predicted_class]}"

        return class_names[predicted_class], tumor_status, confidence

    except Exception as e:
        return None, f"Error processing image: {e}", 0.0

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        file = request.files.get("file")
        if not file or file.filename == "":
            return "No file selected", 400

        filename = file.filename
        file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(file_path)

        prediction, tumor_status, confidence = predict_brain_tumor(file_path)

        return render_template("index.html", result=prediction, tumor_status=tumor_status, confidence=confidence, image=filename)

    return render_template("index.html", result=None,tumor_status=None, confidence=None, image=None)

if __name__ == "__main__":
    app.run(debug=True)
