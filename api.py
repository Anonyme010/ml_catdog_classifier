from fastapi import FastAPI, UploadFile, File
from PIL import Image
import torch
import torchvision.transforms as transforms
import time

from model import ResNet50Binary

app = FastAPI()

# Load model 
model = ResNet50Binary()
model.load_state_dict(torch.load("best_model.pt", map_location="cpu"))
model.eval()

# Transform 
transform = transforms.Compose([
    transforms.Resize((32, 32)),
    transforms.ToTensor(),
])

# API endpoint 
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    input_tensor = transform(image).unsqueeze(0)

    start = time.time()

    with torch.no_grad():
        output = model(input_tensor)
        pred = torch.argmax(output, dim=1).item()

    end = time.time()

    return {
        "prediction": "cat" if pred == 0 else "dog",
        "latency_ms": (end - start) * 1000
    }