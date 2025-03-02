# Brain Tumor Detection Using VGG16

## 📌 Features
✅ **Pre-trained VGG16 model** for accurate classification  
✅ **Flask backend** for real-time predictions  
✅ **User-friendly UI** using HTML, CSS, and JavaScript  
✅ **Supports image uploads** for tumor detection  
✅ **Deployable** on GitHub/Cloud platforms  

---

## 📂 Folder Structure
```
brain_tumor_project/
│── dataset/           # Local dataset (ignored in Git)
│── static/            # Static files (CSS, JS, Images)
│   ├── uploads/       # Uploaded images for prediction
│── templates/         # HTML templates (Flask frontend)
│   ├── index.html     # Main UI for image upload
│── .gitignore         # Ignore unnecessary files (e.g., dataset, .venv)
│── app.py             # Flask backend to handle requests
│── model/             # Pretrained VGG16 model stored here
│── vgg16_brain_tumor.py  # Model training script
│── predict.py         # Script for making predictions
│── requirements.txt   # Dependencies list
│── README.md          # Project documentation
│── saved_models/      # Directory for saving and loading the trained model
```

---

## 🛠️ Setup & Installation

### 1️⃣ Clone the Repository
```
git clone https://github.com/yourusername/braintumordetector_vgg16.git
cd braintumordetector_vgg16
```

### 2️⃣ Create a Virtual Environment *(Optional but Recommended)*
#### For Linux/macOS:
```
python -m venv .venv
source .venv/bin/activate
```
#### For Windows:
```
python -m venv .venv
.venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Run Flask Application
```bash
python app.py
```

📌 **Ensure you create a folder named** `saved_models/` **in the directory to store the trained model.**

🚀 The app will run at: **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)**

---

## 🖼️ Usage
1. Open the web app in your browser.
2. Upload an MRI scan image.
3. The model will predict and display the tumor category.

---

## 🧠 Model Details
- **Architecture:** VGG16 *(Pre-trained on ImageNet)*
- **Fine-tuned on:** Brain Tumor MRI Dataset
- **Classes:**
  - Glioma
  - Meningioma
  - Pituitary
  - No Tumor


