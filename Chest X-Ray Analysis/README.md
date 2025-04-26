#  Automated COVID-19 Detection using Chest X-Ray Images

> A deep learning pipeline built in TensorFlow/Keras to classify 7,135 chest X-ray images into four categories—COVID-19, Pneumonia, Tuberculosis, and Normal—achieving state-of-the-art accuracy with transfer learning.

---

## 📋 Table of Contents

1. [Introduction](#introduction)  
2. [Dataset](#dataset)  
3. [Environment & Dependencies](#environment--dependencies)  
4. [Directory Structure](#directory-structure)  
5. [Quick Start](#quick-start)  
6. [Model Architectures](#model-architectures)  
7. [Training & Validation](#training--validation)  
8. [Results & Performance](#results--performance)  
9. [Inference](#inference)  
10. [Confusion Matrices](#confusion-matrices)  
12. [References](#references)  


---

## 🔍 Introduction

This project demonstrates how to leverage **transfer learning** with the VGG16 architecture to boost performance on a multi-class medical image classification problem. We compare:

- **CNN from scratch** (20 epochs)  
- **VGG16 + Transfer Learning** (10 epochs)

Key achievements:

- **81.97%** test accuracy with VGG16  
- **+31.39%** improvement over baseline CNN (50.58% accuracy)  
- **<1 second** inference time per scan  

---

## Dataset

- **Source**: [Kaggle – Chest X-Ray Pneumonia, COVID-19, Tuberculosis](https://www.kaggle.com/datasets/jtiptj/chest-x-ray-pneumoniacovid19tuberculosis)  
- **Total images**: 7,135  
  - **Train**: 6,326 images (4 classes)  
  - **Validation**: 383 images  
  - **Test**: 771 images  
- **Classes**: `COVID-19`, `PNEUMONIA`, `TUBERCULOSIS`, `NORMAL`

---

## Environment & Dependencies

- **Python**: 3.8+  
- **TensorFlow**: 2.x (tested on 2.10.0)  
- **Keras API**, **NumPy**, **Matplotlib**, **Seaborn**, **scikit-learn**  
- **Google Colab** (with GPU) or any CUDA-enabled environment  
- **kagglehub** (for dataset download)  

```bash
pip install tensorflow numpy matplotlib seaborn scikit-learn kagglehub



```
##  Directory Structure
.
├── README.md
├── VGG16_From_Scratch.ipynb       # Executable Colab notebook
├── chest_xray_code_vgg16.py       # Script version
├── requirements.txt               # Python dependencies
└── data/
    ├── train/                     # 4 subfolders: COVID-19, NORMAL, PNEUMONIA, TUBERCULOSIS
    ├── val/
    └── test/
```

```

##  Quick Start

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/covid-xray-classification.git
   cd covid-xray-classification
   ```

2. **Install requirements**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Download data** (in Colab):  
   ```python
   import kagglehub
   path = kagglehub.dataset_download("jtiptj/chest-xray-pneumoniacovid19tuberculosis")
   ```

4. **Run the notebook** or **execute the script**:  
   ```bash
   python chest_xray_code_vgg16.py --data_dir /path/to/data
   ```



##  Model Architectures

### 1. CNN from Scratch

- 13 convolutional layers + pooling inspired by VGG16  
- Trained for **20 epochs**  
- Final **Test Accuracy**: **50.58%**

### 2. VGG16 with Transfer Learning

- Loaded **ImageNet** weights, `include_top=False`  
- **Frozen** all convolutional layers  
- Added custom dense head (512 units + dropout)  
- Trained for **10 epochs** at `lr=1e-4`  
- Final **Test Accuracy**: **81.97%**  

---

##  Training & Validation

- **Batch Size**: 32  
- **Image Size**: 224×224 pixels  
- **Data Augmentation**:  
  - Random flips (horizontal & vertical)  
  - Random rotations (±20%)  
- **Optimizer**: Adam  
- **Loss**: Sparse Categorical Crossentropy  
- **Validation Split**: Pre-defined 383 images  

---

##  Results & Performance

| Model                      | Train Acc. | Val Acc. | Test Acc. | Improvement |
|----------------------------|-----------:|---------:|----------:|------------:|
| CNN (from scratch)         | 61.51%     | 21.05%   | 50.58%    | –           |
| VGG16 (transfer learning)  | 93.86%     | 84.21%   | 81.97%    | +31.39%     |

- **Best Val. Acc.**: 92.11% (epoch 5, VGG16)  
- **Inference**: <1 s/image on Colab GPU  

---

##  Inference

```python
# Load trained model
model = tf.keras.models.load_model("covid_xray_model.h5")

# Predict on a single image
from tensorflow.keras.preprocessing import image
img = image.load_img("test/COVID-19/img1.png", target_size=(224,224))
x   = image.img_to_array(img)/255.0
pred = model.predict(x[np.newaxis, ...])
print("Predicted class:", np.argmax(pred), "Confidence:", np.max(pred))
```

---

##  Confusion Matrices

![Confusion Matrices](confusion_matrices.png)  
*(Train • Validation • Test)*

---


## References

1. Simonyan, K. & Zisserman, A. “Very Deep Convolutional Networks for Large-Scale Image Recognition.” arXiv (2014).  
2. Kaggle dataset by jtiptj :  https://www.kaggle.com/datasets/jtiptj/chest-xray-pneumoniacovid19tuberculosis

---

