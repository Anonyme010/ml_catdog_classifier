# ML Cat vs Dog Classifier - Project Plan

## Project Goal
Build a binary image classification model to classify CIFAR-10 images as cats or dogs.

## What We're Building

### Overall Architecture
- **Model**: ResNet50 (pretrained on ImageNet)
- **Dataset**: CIFAR-10 (binary classification: cats vs dogs)
- **Framework**: PyTorch 2.0.1 + TorchVision 0.15.2
- **Training Environment**: Google Colab T4 GPU
- **Languages & Tools**: Python, Jupyter Notebook, Git

### Project Components

**1. Data Pipeline**
- Load CIFAR-10 dataset automatically
- Filter for cats  and dogs 
- Clean corrupted images 
- Create stratified train/val/test splits (80/10/10)
- Apply data augmentation (flips, rotations, color jitter)

**2. Model Architecture**
- ResNet50 backbone (pretrained on ImageNet)
- Custom binary classification head
- Architecture: 2048 → 512 → 256 → 2 (with ReLU and Dropout)
- Total parameters: 24.7M

**3. Training Pipeline**
- Loss function: CrossEntropyLoss + L2 regularization
- Optimizer: Adam (lr=0.001, weight_decay=0.0001)
- Learning rate scheduler: ReduceLROnPlateau
- Early stopping: patience=5 epochs
- Gradient clipping: max_norm=1.0

**4. Evaluation & Analysis**
- Compute metrics: Accuracy, Precision, Recall, F1-Score, ROC-AUC
- Generate confusion matrix
- Create training curves visualization
- Analyze failure modes and error patterns
- Save model checkpoint

## Expected Outcomes
- Test Accuracy: ~80%+
- F1-Score: ~0.79+
- ROC-AUC: ~0.89+
- Training time: ~39 minutes on Colab T4

## Project Structure
```
ml-cat-dog-classifier/
├── notebooks/Project.ipynb       # Complete pipeline
├── config.yaml                      # Hyperparameters
├── requirements.txt                 # Dependencies (pinned versions)
├── README.md                        # Project documentation
├── initials.md                      # Documented initialisation 
└── .gitignore                       # Git ignore patterns
```

### ✓ Commit 1: Initial Project Setup
**Description:** Foundation and setup files for the ML project.


### ✓ Commit 2: Data Pipeline & Model Architecture 
**Description:** Implement data loading, preprocessing, and model architecture.
