# Flask Face Verification

A simple Flask application for face verification using DeepFace library.

## Description

This application allows users to verify their identity by uploading an image. The uploaded image is compared against a pre-stored image associated with the user ID provided. If the faces in the two images match, the user is verified.

## Installation

1. Clone this repository:

2. Navigate to the project directory:


3. Install the required dependencies:

## Usage

1. Run the Flask application:



2. Open a web browser and go to [http://localhost:5000](http://localhost:5000).

3. Upload an image to verify your identity by providing your user ID and selecting the image file.

## Endpoints

- `POST /verify`: Verifies a user's face by comparing the uploaded image against the known face image associated with the provided user ID.
- Request Parameters:
 - `user_id`: ID of the user.
 - `file`: Image file to be uploaded.
- Response: Returns the verification result along with the user ID and distance.

- `POST /add_user`: Adds a new user to the database by saving the uploaded image as the known face image associated with the provided user ID.
- Request Parameters:
 - `user_id`: ID of the user.
 - `file`: Image file to be uploaded.
- Response: Returns a message confirming the successful addition of the user.

## Directory Structure

- `app.py`: Main Flask application file containing the routes and logic.
- `database/`: Directory to store user data.
- `templates/`: HTML templates for the web interface.

