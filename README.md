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

```bash
python quant_image.py
