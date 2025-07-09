import tensorflow as tf

# Load a pre-trained model
model = tf.keras.applications.MobileNetV2(weights='imagenet', input_shape=(224, 224, 3))

# Convert to TFLite with quantization
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Convert
tflite_quant_model = converter.convert()

# Save the quantized model
with open('mobilenet_quant.tflite', 'wb') as f:
    f.write(tflite_quant_model)

print("✅ Saved quantized model as model_quant.tflite")
