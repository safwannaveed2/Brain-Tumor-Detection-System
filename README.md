🧠 Brain Tumor Detection System (AI Powered)
📌 Overview

This project implements an AI-powered Brain Tumor Detection System using Deep Learning and Transfer Learning. A pre-trained Convolutional Neural Network (CNN) analyzes brain MRI images and predicts whether a tumor is present or not, along with a confidence score. The system is designed for educational and research purposes.

🎯 Objectives

Learn and apply Deep Learning & CNNs

Use Transfer Learning with pre-trained models

Perform Binary Image Classification

Build an interactive Gradio-based UI

Deploy and demonstrate a real-world medical imaging application

🧠 Dataset

The model is trained on an open-source Brain MRI Dataset containing two classes:

Tumor

No Tumor

Images are preprocessed and split into:

Training set (70%)

Validation set (15%)

Test set (15%)

🏗️ Model Architecture

Base Model: EfficientNetB0 (pre-trained on ImageNet)

Approach: Transfer Learning

Base layers frozen during initial training

Custom classification head added:

Global Average Pooling

Dense layer with sigmoid activation

Loss Function: Binary Crossentropy

Optimizer: Adam

Evaluation Metric: Accuracy

🖥️ User Interface

The application uses Gradio for the frontend:

MRI image upload

One-click prediction

Clear result display:

Tumor / No Tumor

Confidence percentage

Fully compatible with Google Colab

🚀 How It Works

User uploads a brain MRI image

Image is resized and preprocessed

The trained CNN model analyzes the image

The system outputs:

Prediction result

Confidence score
