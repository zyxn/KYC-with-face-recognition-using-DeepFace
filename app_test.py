import os
import pytest
import requests
import shutil
import time
# Endpoint URL
url = 'http://localhost:5000/add_user'
url_verif = 'http://localhost:5000/verify'

def test_add_user_with_photo():
    # Provide a user ID and an image file
    user_id = 'test_user'
    image_path = './test_file/cat.jpg'
    files = {'file': open(image_path, 'rb')}
    data = {'user_id': user_id}

    # Send POST request to the endpoint
    response = requests.post(url, files=files, data=data)

    # Check if the user is added successfully
    assert response.status_code == 200
    assert response.json()['message'] == 'User added successfully'
    assert response.json()['user_id'] == user_id
    time.sleep(1)
    shutil.rmtree("./database/test_user")   
    
    
    

def test_add_user_without_photo():
    # Provide a user ID without an image file
    user_id = 'test_user'
    data = {'user_id': user_id}

    # Send POST request to the endpoint
    response = requests.post(url, data=data)

    # Check if the endpoint returns an error
    assert response.status_code == 400
    assert response.json()['error'] == 'File and user_id are required'
    

def test_verified():
    # Provide a user ID without an image file
    user_id = '1301'
    image_path = './test_file/test1.jpeg'
    files = {'file': open(image_path, 'rb')}
    data = {'user_id': user_id}
    
    # Send POST request to the endpoint
    response = requests.post(url_verif,files=files, data=data)

    # Check if the endpoint returns an error
    assert response.status_code == 200
    assert response.json()['user_id'] == user_id
    assert response.json()['result'] == 'Verified'

def test_verified_without_photo():
    # Provide a user ID without an image file
    user_id = '1301'
    data = {'user_id': user_id}
    
    # Send POST request to the endpoint
    response = requests.post(url_verif, data=data)

    # Check if the endpoint returns an error
    assert response.status_code == 400
    assert response.json()['error'] == "File and user_id are required"
    
    
def test_verified_false_id():
    # Provide a user ID without an image file
    user_id = 'false'
    data = {'user_id': user_id}
    
    # Send POST request to the endpoint
    response = requests.post(url_verif, data=data)

    # Check if the endpoint returns an error
    assert response.status_code == 400
    assert response.json()['error'] == "File and user_id are required"

if __name__ == '__main__':
    pytest.main()
