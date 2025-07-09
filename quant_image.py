

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# Load and display an image
img = Image.open('xyzzz.jpg').convert('RGB')
img = img.resize((256, 256))  # Resize for simplicity
img_np = np.array(img)

# Quantization function: Reduce 8-bit (0–255) to 4-bit (0–15)
def quantize_image(img, levels=16):
    factor = 256 // levels
    quantized = (img // factor) * factor
    return quantized

quantized_img = quantize_image(img_np, levels=16)

# Show original vs quantized
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(img_np)
plt.title("Original Image (256 levels)")

plt.subplot(1, 2, 2)
plt.imshow(quantized_img)
plt.title("Quantized Image (16 levels)")
plt.savefig("quantized_output.png")
print("Plot saved as quantized_output.png")
