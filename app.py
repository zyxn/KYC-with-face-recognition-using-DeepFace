from flask import Flask, request, jsonify
import cv2
import numpy as np
from deepface import DeepFace
import os
import imghdr

app = Flask(__name__)


db_path = 'database'

@app.route('/verify', methods=['POST'])
def verify_face():
    if 'file' not in request.files or 'user_id' not in request.form:
        return jsonify({'error': 'File and user_id are required'}), 400
    
    user_id = request.form['user_id']
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    user_folder = os.path.join(db_path, user_id)
    print(f"Checking user folder: {user_folder}") 

    if not os.path.exists(user_folder):
        return jsonify({'error': 'User ID not found'}), 404

    # Determine file extension and create known face path
    file_extension = imghdr.what(file)
    if file_extension is None:
        return jsonify({'error': 'Unknown file format'}), 400
    
    known_face_path = os.path.join(user_folder, f'known_face.{file_extension}')
    print(f"Known face path: {known_face_path}") 

    if not os.path.exists(known_face_path):
        return jsonify({'error': 'Known face image not found'}), 404


    npimg = np.frombuffer(file.read(), np.uint8)
    img = cv2.imdecode(npimg, cv2.IMREAD_COLOR)


    known_face_img = cv2.imread(known_face_path)

    if known_face_img is None:
        return jsonify({'error': 'Known face image could not be read'}), 500

    try:

        result = DeepFace.verify(img, known_face_img, model_name="VGG-Face",detector_backend='mediapipe')
    except Exception as e:
        return jsonify({'error': 'Face verification failed', 'message': str(e)}), 500


    if result["verified"]:
        return jsonify({'result': 'Verified', 'user_id': user_id, 'distance': result['distance']})
    else:
        return jsonify({'result': 'No Verified', 'distance': result['distance']})



@app.route('/add_user', methods=['POST'])
def add_user():

    if 'file' not in request.files or 'user_id' not in request.form:
        return jsonify({'error': 'File and user_id are required'}), 400
    
    user_id = request.form['user_id']
    file = request.files['file']


    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    user_folder = os.path.join(db_path, user_id)
    if not os.path.exists(user_folder):
        os.makedirs(user_folder)

    file_path = os.path.join(user_folder, 'known_face.jpg')
    file.save(file_path)

    return jsonify({'message': 'User added successfully', 'user_id': user_id})


@app.route('/')
def index():
    return '''
    <!doctype html>
    <title>Face Verification</title>
    <h1>Upload an Image to Verify</h1>
    <form method="post" action="/verify" enctype="multipart/form-data">
      User ID: <input type="text" name="user_id"><br><br>
      <input type="file" name="file"><br><br>
      <input type="submit" value="Verify">
    </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
