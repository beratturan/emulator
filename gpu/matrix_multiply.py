import tensorflow as tf
import os
import time

# Read the MATRIX_SIZE environment variable or use a default value
matrix_size = int(os.environ.get('MATRIX_SIZE', 1000))

# Check if GPU is available
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Generate random matrices
matrix_a = tf.random.normal((matrix_size, matrix_size))
matrix_b = tf.random.normal((matrix_size, matrix_size))

# Define a simple matrix multiplication function
def matrix_multiply():
    result = tf.matmul(matrix_a, matrix_b)

# Run the matrix multiplication on the GPU and measure the time
with tf.device('/GPU:0'):
    start_time = time.time()
    matrix_multiply()
    end_time = time.time()

print(f"Time taken on GPU: {end_time - start_time} seconds")
