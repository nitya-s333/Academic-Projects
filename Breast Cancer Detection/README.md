---
#  Breast Cancer Detection using Machine Learning (Wisconsin & Coimbra)

##  Project Overview
The goal of this project was to perform a **comparative study** of various machine learning algorithms to **detect breast cancer** using two real-world datasets:  
- The **Wisconsin Breast Cancer Dataset** (structured, detailed feature set)  
- The **Coimbra Breast Cancer Dataset** (small, vague features dataset)
We aimed to determine which algorithm performs best for each dataset and to explore how **ensemble techniques like Bagging and Stacking** can further improve model performance.

---

##  Objectives
- **Preprocess** the data (handle missing values, scaling, etc.)
- **Train** models like:
  - Decision Tree
  - K-Nearest Neighbors (KNN)
  - Naïve Bayes
  - Random Forest
  - Bagging Classifier
  - Stacking Classifier
- **Optimize** Random Forest models using **GridSearchCV** (hyperparameter tuning)
- **Evaluate** using metrics: Accuracy, Precision, Recall, F1-score, ROC AUC
- **Compare** model performances across both datasets
- **Identify** the best algorithm for each dataset and analyze the results.

---

## Datasets Used
- **Wisconsin Breast Cancer Dataset**  
  > - 569 samples, 30 features (mean, texture, perimeter, area etc.)  
  > - Labels: Benign (0) or Malignant (1)
  
- **Coimbra Breast Cancer Dataset**  
  > - 116 samples, 9 features (BMI, glucose, age, insulin etc.)  
  > - Labels: Healthy (1) or Cancer (2)

---

##  Methodology
1. **Data Preprocessing**  
   - Handled missing values using **SimpleImputer** with 'median' strategy.
   - **Standardized** features with **StandardScaler**.
2. **Model Training and Testing**  
   - Trained each model on the training set, evaluated on the test set.
3. **Ensemble Methods**  
   - **Bagging**: Random Forest-based Bagging.
   - **Stacking**: Combined Random Forest, SVM, and Logistic Regression.
4. **Hyperparameter Tuning**  
   - **Random Forest** tuned using **GridSearchCV**.
5. **Evaluation Metrics**  
   - Accuracy, Precision, Recall, F1-Score, ROC AUC.

---

## Results Summary

| Model             | Dataset   | Accuracy | Precision | Recall | F1-Score | ROC AUC |
|-------------------|-----------|----------|-----------|--------|----------|---------|
| Random Forest (Default) | Wisconsin | 97.08%  | 97.36%    | 96.36% | 96.83%   | 99.69%  |
| Random Forest (Tuned)   | Wisconsin | 96.49%  | 96.54%    | 95.90% | 96.20%   | 99.62%  |
| **Stacking (Best)**     | Wisconsin | **97.66%** | **97.49%** | **97.49%** | **97.49%** | **99.78%** |
| Random Forest (Default) | Coimbra   | 71.43%  | 71.41%    | 71.41% | 71.41%   | 80.56%  |
| Random Forest (Tuned)   | Coimbra   | 68.57%  | 68.63%    | 68.63% | 68.57%   | 80.23%  |
| **Stacking (Best)**     | Coimbra   | **77.14%** | **77.50%** | **76.96%** | **76.97%** | **83.01%** |

> **Stacking Classifier** outperformed all other models on both datasets.

---

##  Key Findings
- **Wisconsin Dataset**:  
  > Stacking achieved **97.66%** accuracy, highest among all models.
- **Coimbra Dataset**:  
  > Stacking improved accuracy to **77.14%**, about **6% higher** than simple Random Forest baseline.
- **Bagging** helped in stabilizing Random Forest predictions slightly but **Stacking** gave the most significant boost.
- **Random Forest tuning** using GridSearchCV slightly worsened results due to dataset size and overfitting on small datasets (especially Coimbra).

---

##  Technologies Used
- Python
- Scikit-learn
- Pandas, NumPy
- Matplotlib, Seaborn

---

## How to Run
1. Clone the repository
2. Install required libraries
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook

---

##  Conclusion
A **Stacking Classifier** combining multiple models performed **the best** for breast cancer prediction on both detailed (Wisconsin) and vague (Coimbra) datasets.  
The project shows how **ensemble learning** can significantly enhance predictive performance even on small healthcare datasets.

