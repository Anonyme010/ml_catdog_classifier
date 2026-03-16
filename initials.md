# ML Cat vs Dog Classifier - Project Plan

## Project Goal
Build a binary image classification model to classify CIFAR-10 images as cats or dogs.

## What We're Building

### Overall Architecture
- **Model**: ResNet50 (pretrained on ImageNet)
- **Dataset**: CIFAR-10 (binary classification: cats vs dogs)
- **Framework**: PyTorch + TorchVision (gooleColab)
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

### ✓  Commit 3: Training & Evaluation (READY TO PUSH)
**Description:** Training pipeline, evaluation, and visualizations


## Key Results

| Metric | Value |
|--------|-------|
| Test Accuracy | 80.70% |
| Precision | 0.8499 |
| Recall | 0.7419 |
| F1-Score | 0.7922 |
| ROC-AUC | 0.8909 |


**Error Pattern:**
68 cat→dog confusion
131 dog→cat confusion

## Training Execution

All training done in Google Colab notebook (`notebooks/Project.ipynb`):
1. Installs dependencies
2. Downloads CIFAR-10
3. Cleans & preprocesses data
4. Creates model
5. Trains with early stopping
6. Evaluates on test set
7. Generates visualizations

Run with: Open notebook in Colab → Ctrl+F9 (Run all)


## Results & Artifacts

Results from the training run are stored in the `downloaded_results/` folder:

- `best_model.pt` - Best model checkpoint (saved at epoch 21)
- `training_curves.png` - Plot of training and validation loss/accuracy over epochs
- `confusion_matrix.png` - Confusion matrix visualization on test set
- `roc_curve.png` - ROC curve with AUC score
- `training.log` - Complete training log with epoch-by-epoch metrics

**Author:** HASNAOUI Walid , github username : "Anonyme010"