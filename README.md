# Quantization Techniques in Python

This repository demonstrates two practical applications of **quantization**:

1. **Image Quantization**: Reducing color depth of an image.
2. **Model Quantization**: Compressing a TensorFlow model using TFLite for edge deployment.

---

## 📁 Files

| File            | Description                                               |
|-----------------|-----------------------------------------------------------|
| `quant_image.py`| Performs image color quantization from 256 to N levels.   |
| `quant_model.py`| Applies post-training quantization to a Keras model.      |
| `requirements.txt` | Required Python packages for running the scripts.      |
| `results/`      | Contains output image from quantization.                 |

---

## 🧪 1. Image Quantization

### 📌 Purpose

Reduce an image’s color depth (e.g., from 256 to 16 levels per channel) and observe visual tradeoffs.

### 🚀 How to Run


python quant_image.py




Make sure your_image.jpg is present or modify the script to use another image.
💾 Output
quantized_output.png


##  🤖 2. Model Quantization (TensorFlow)

### 📌 Purpose
Use TensorFlow Lite to compress a Keras model for edge devices.

###  🚀 How to Run
python quant_model.py



## 📦 Installation

Install dependencies:

pip install -r requirements.txt
If you're using a virtual environment:

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


## 📚 References

TensorFlow Lite Quantization
Matplotlib
