# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest-gpu

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container
COPY . .

# Install any dependencies you may need
RUN pip install --no-cache-dir -q tensorflow

# Run matrix multiplication when the container launches
CMD ["python", "./matrix_multiply.py"]
