import os
import numpy as np
import cv2
import gdown
import tensorflow as tf
from flask import Flask, render_template, request

app = Flask(__name__)


UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

MODEL_DIR = "saved_model"
MODEL_FILENAME = "brain_tumor_vgg16_final.keras"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_FILENAME)

# Google Drive model link 
GDRIVE_FILE_ID = "1Co9f69uzYq6BmPrvg9ObRhdHQ8sbNW1q"
GDRIVE_URL = f"https://drive.google.com/uc?id={GDRIVE_FILE_ID}"

os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    try:
        gdown.download(GDRIVE_URL, MODEL_PATH, quiet=False)
        print(" Model downloaded successfully!")
    except Exception as e:
        print(f"Error downloading model: {e}")
        exit(1)  

# Loading trained model
try:
    model = tf.keras.models.load_model(MODEL_PATH, compile=False)
    print(" Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    exit(1)

class_names = ["Glioma", "Meningioma", "No Tumor", "Pituitary"]

# predicting brain tumor
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

# Flask routes
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

    return render_template("index.html", result=None, tumor_status=None, confidence=None, image=None)
#Flask running
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)
