# 🧠 Brain Tumor Detection System (AI Powered)

This project is a **Deep Learning-based Brain Tumor Detection System** using **MRI images**.  
It uses **Transfer Learning** with a **pre-trained CNN** to classify brain MRI scans as **Tumor** or **No Tumor**.

---

## 🔹 Features

- Upload a brain MRI image
- Detect whether a tumor is present
- Display **confidence score**
- Fast and accurate predictions
- Easy-to-use **Gradio interface**

---

## 🔹 Technologies Used

- **TensorFlow / Keras** – Deep Learning
- **MobileNetV2** – Pre-trained CNN for Transfer Learning
- **Gradio** – Interactive Web App
- **Python** – Programming language
- **NumPy, Pillow** – Image processing

---
## 🔹 Model Details

- **Base Model:** MobileNetV2 (pre-trained on ImageNet)
- **Transfer Learning:** Base layers frozen
- **Custom Layers:** GlobalAveragePooling2D + Dense layers for binary classification
- **Activation:** Sigmoid (for Tumor / No Tumor)
- **Saved Model:** `model/brain_tumor_model.keras`

**Accuracy Achieved:** ~95% on validation data (may vary slightly based on dataset split)
