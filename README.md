# AI Garbage Classification 

## Overview
This project aims to classify different types of garbage using an AI model deployed as a web application. The AI model is trained to categorize garbage into four main categories: Kitchen Waste, Recyclables, Other Waste, and Hazardous Waste. The web application allows users to upload images of garbage, which are then processed by the AI model to determine the appropriate category.

## Technologies Used
- **Frontend**:
  - Next.js: Used for building the user interface and handling interactions.
  - Tailwind CSS: A utility-first CSS framework for styling the components.
  - TypeScript: Provides static typing and improved code readability.
  - [Uploadthing](https://uploadthing.com/dashboard/yhjuizblen): A file upload widget used to handle image uploads on the frontend.

- **Backend**:
  - Flask: A Python web framework used for creating the API endpoint to classify garbage images.
  - PyTorch: A deep learning framework used to develop and train the garbage classification AI model.
  - MobileNetV3: A pre-trained neural network model used as the base for garbage classification.

- **Deployment**:
  - Vercel: Used to deploy the frontend Next.js application.
  - [Render](https://dashboard.render.com/): Used to deploy the Flask API endpoint for garbage classification.

## Project Structure
The project consists of two main components:

1. **Frontend**:
   - The frontend is built using React.js with Next.js for server-side rendering.
   - Users can upload images of garbage through a user-friendly interface.
   - The uploaded images are sent to the backend API for classification.

2. **Backend**:
   - The backend is built using Flask, a lightweight Python web framework.
   - An API endpoint `/api/classify` is created to handle image classification requests.
   - The API uses a pre-trained AI model based on MobileNetV3 to classify garbage images into the appropriate categories.

## Getting Started
To run the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/cqlyj/garbage-classification.git`
2. Navigate to the project directory: `cd garbage-classification`
3. Install dependencies for the frontend:
   ```
   cd frontend
   npm install
   ```
4. Install dependencies for the backend:
   ```
   cd backend
   pip install -r requirements.txt
   ```
5. Start the frontend development server:
   ```
   cd frontend
   npm run dev
   ```
6. Start the backend server:
   ```
   cd backend
   python3 app.py
   ```
7. Access the web application in your browser at `http://localhost:3000`

## Usage
1. Upload an image of garbage using the provided interface on the web application.
2. Wait for the AI model to process the image and classify it into one of the four categories.
3. View the classification result displayed on the screen.

## License
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).