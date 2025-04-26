

---

#  Breast Cancer Detection using Machine Learning (Wisconsin & Coimbra)

## Project Overview
The project aimed to perform a **comparative study** of machine learning models for **breast cancer prediction**, using two datasets:  
- **Wisconsin Breast Cancer Dataset** (structured, detailed features)  
- **Coimbra Breast Cancer Dataset** (smaller, vague features)

We identified the best model using both **traditional** and **ensemble** techniques (Bagging and Stacking).

---

##  Objectives
- Preprocess datasets (handle missing values, scale features)
- Train classifiers: Decision Tree, KNN, Naïve Bayes, Random Forest
- Apply ensemble methods: Bagging, Stacking
- Tune hyperparameters via GridSearchCV
- Evaluate models with metrics: Accuracy, Precision, Recall, F1-score, ROC AUC

---

## 🗂 Datasets
- **Wisconsin Breast Cancer Dataset**  
  > - 569 samples, 30 features  
  > - Labels: Benign (0) / Malignant (1)
- **Coimbra Breast Cancer Dataset**  
  > - 116 samples, 9 features  
  > - Labels: Healthy (1) / Cancer (2)

---

## Methodology
1. **Missing value imputation** with median strategy
2. **Feature scaling** using StandardScaler
3. **Model building** with pipelines
4. **Hyperparameter tuning** using GridSearchCV
5. **Performance evaluation** on test sets

---

##  Results

| Model             | Dataset   | Accuracy | Precision | Recall | F1-Score | ROC AUC |
|-------------------|-----------|----------|-----------|--------|----------|---------|
| Random Forest (Default) | Wisconsin | 97.08% | 97.36% | 96.36% | 96.83% | 99.69% |
| Random Forest (Tuned)   | Wisconsin | 96.49% | 96.54% | 95.90% | 96.20% | 99.62% |
| **Stacking (Best)**     | Wisconsin | **97.66%** | **97.49%** | **97.49%** | **97.49%** | **99.78%** |
| Random Forest (Default) | Coimbra   | 71.43% | 71.41% | 71.41% | 71.41% | 80.56% |
| Random Forest (Tuned)   | Coimbra   | 68.57% | 68.63% | 68.63% | 68.57% | 80.23% |
| **Stacking (Best)**     | Coimbra   | **77.14%** | **77.50%** | **76.96%** | **76.97%** | **83.01%** |

---

##  Key Insights
- **Stacking Classifier** outperformed all other models for both datasets.
- On **Coimbra dataset**, stacking improved accuracy by ~6% over simple Random Forest.
- **Bagging** stabilized Random Forest predictions but did not outperform stacking.

---

## Tech Stack
- Python
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn

---

##  Conclusion
**Stacking classifiers combining multiple models** achieved **the best prediction performance**, proving that ensemble learning significantly enhances cancer detection on structured and small-feature datasets.

---
