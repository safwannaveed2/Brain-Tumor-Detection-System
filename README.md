🧠 Brain Tumor Detection System using Deep Learning

A deep learning–based medical imaging project that detects the presence of a brain tumor from MRI scans using a Convolutional Neural Network (CNN) with transfer learning (EfficientNet).
The system is designed for educational and research purposes and demonstrates an end-to-end ML pipeline from data preprocessing to model training and inference.

📌 Project Overview

Brain tumors are life-threatening and require early diagnosis. This project aims to assist in automated brain tumor detection by classifying MRI images into:

Tumor (Yes)

No Tumor (No)

The model leverages EfficientNetB0, a powerful pre-trained CNN architecture, to achieve high accuracy with limited training data.

🚀 Features

MRI image classification (Tumor / No Tumor)

Transfer Learning using EfficientNetB0

Data augmentation for better generalization

Fine-tuning of deep layers

Binary classification with confidence scores

Ready for deployment (Streamlit / Gradio compatible)

🧠 Model Architecture

Base Model: EfficientNetB0 (ImageNet weights)

Custom Layers:

Global Average Pooling

Dense (ReLU)

Dropout (regularization)

Sigmoid output layer

Loss Function: Binary Crossentropy

Optimizer: Adam

Input Size: 224 × 224 × 3

📂 Dataset Structure
brain_tumor_small/
│
├── train/
│   ├── yes/
│   └── no/
│
├── validation/
│   ├── yes/
│   └── no/
│
└── test/
    ├── yes/
    └── no/


Dataset consists of MRI images labeled as Tumor (yes) and No Tumor (no).
