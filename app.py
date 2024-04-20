from io import BytesIO
from flask import Flask, jsonify, render_template, request
import torch
import requests
from PIL import Image
from torchvision import transforms
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.backends.cudnn as cudnn
import numpy as np
from torchvision import models, transforms
import matplotlib.pyplot as plt

checkpoint = torch.load("model/80735.pt", map_location=torch.device("cpu"))
model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)
num_ftrs = model.classifier[-1].in_features
model.fc = nn.Linear(num_ftrs, 265)
model.load_state_dict(checkpoint["model_state_dict"])
model.eval()


app = Flask(__name__)


@app.route("/api/classify", methods=["POST"])
def classify():
    data_transform = transforms.Compose(
        [
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ]
    )

    # Get the image URL from the JSON data in the POST request
    json_data = request.get_json()
    image_url = json_data.get("url")

    # Download the image from the URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert("RGB")
    image = data_transform(image)
    image = image.unsqueeze(0)

    classification = model(image)
    _, predicted = torch.max(classification, 1)
    predictedLabel = predicted[0].item()
    # return predictedLabel
    return jsonify({"predicted_label": str(predictedLabel)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
