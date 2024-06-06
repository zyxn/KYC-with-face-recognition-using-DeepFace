# Gunakan base image Python yang sudah mencakup Flask
FROM python:3.8-slim

# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Install dependensi

# Menyalin kode aplikasi Anda ke dalam image
COPY . /app
WORKDIR /app
COPY ~/.deepface/weights/. ~/.deepface/weights/

RUN pip install -r requirements.txt
# Expose port 5000
EXPOSE 5000

# Perintah untuk menjalankan server Flask
CMD ["python", "app.py"]
