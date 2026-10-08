import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

ROOT = Path(__file__).resolve().parents[1]
ROLL = 'BT2024155'

CONFIG = {
    'var1': {'features': ['x1', 'x2', 'x3'], 'degree': 3},
    'var2': {'features': ['x1'], 'degree': 4},
}

for var, cfg in CONFIG.items():
    train = pd.read_csv(ROOT / f'{ROLL}_train_{var}.csv')
    test = pd.read_csv(ROOT / f'{ROLL}_test_{var}.csv')
    X_train = train[cfg['features']]
    y_train = train['y']
    X_test = test[cfg['features']]

    model = Pipeline([
        ('poly', PolynomialFeatures(degree=cfg['degree'], include_bias=False)),
        ('regressor', LinearRegression()),
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    pd.DataFrame({'y': pred}).to_csv(ROOT / 'results' / f'{ROLL}_pred_{var}.csv', index=False)
    print(f'{var}: degree={cfg["degree"]}, features={cfg["features"]}, predictions={len(pred)}')
