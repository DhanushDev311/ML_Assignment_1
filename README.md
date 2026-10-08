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
```

## Requirements

- Python 3.x
- NumPy
- Pandas
- Scikit-learn

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

## Running the Code

Run the following command from the project root:

```bash
python src/train_and_predict.py
```

The script trains the polynomial regression models using the provided training datasets and generates predictions for the corresponding test datasets.

The prediction files are saved in the `results/` directory:

```text
results/BT2024155_pred_var1.csv
results/BT2024155_pred_var2.csv
```

Each prediction file contains a single column named `y`.

## Results

The generated prediction files contain the predicted `y` values for the corresponding test datasets. The final models are trained using the complete training datasets.

Detailed methodology and model selection are provided in the assignment report:

```text
report/BT2024155_Assignment1_Report.pdf
```
