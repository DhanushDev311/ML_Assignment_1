# Machine Learning Assignment 1

## Polynomial Regression

This repository contains the implementation and prediction results for **Assignment 1**.

The assignment involves training polynomial regression models on two provided datasets (`var1` and `var2`) and generating predictions for their corresponding test datasets.

## Models

| Dataset | Features | Polynomial Degree |
| ------- | -------- | ----------------- |
| `var1` | `x1, x2, x3` | 3 |
| `var2` | `x1` | 4 |

The models are implemented using **scikit-learn** with polynomial feature expansion followed by linear regression.

## Project Structure

```text
BT2024155/
├── src/
│   └── train_and_predict.py
├── results/
│   ├── BT2024155_pred_var1.csv
│   └── BT2024155_pred_var2.csv
├── BT2024155_train_var1.csv
├── BT2024155_test_var1.csv
├── BT2024155_train_var2.csv
├── BT2024155_test_var2.csv
├── report/
│   └── BT2024155_Assignment1_Report.pdf
├── requirements.txt
└── README.md
