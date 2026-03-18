import torch
import torch.nn as nn
import torchvision.models as models

class ResNet50Binary(nn.Module):
    def __init__(self, num_classes=2, dropout_rate=0.5):
        super().__init__()

        resnet50 = models.resnet50(pretrained=False)  

        self.backbone = nn.Sequential(*list(resnet50.children())[:-1])

        self.head = nn.Sequential(
            nn.Flatten(),
            nn.Linear(2048, 512),
            nn.ReLU(),
            nn.Dropout(p=dropout_rate),
            nn.Linear(512, 256),
            nn.ReLU(),
            nn.Dropout(p=dropout_rate),
            nn.Linear(256, num_classes)
        )

    def forward(self, x):
        features = self.backbone(x)
        logits = self.head(features)
        return logits