# 🛒 Store Sales — Time Series Forecasting

> Kaggle Competition: [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)

## 📌 Overview

This project aims to predict the sales of thousands of product families sold at Favorita stores located in Ecuador. The training data includes dates, store and product information, promotional information, and sales figures. The goal is to build accurate time series models that generalize well to future sales.

## 🎯 Objective

Build a model to **forecast store-level product family sales** using historical data, supplementary metadata (oil prices, holidays, transactions), and promotional flags.

## 📁 Project Structure

```
store-sales-forecasting/
│
├── data/
│   ├── raw/               # Original Kaggle datasets (not tracked by git)
│   ├── processed/         # Cleaned and feature-engineered datasets
│   └── external/          # External data sources (oil, holidays, etc.)
│
├── notebooks/
│   ├── 01_eda.ipynb        # Exploratory Data Analysis
│   ├── 02_feature_engineering.ipynb
│   ├── 03_baseline_model.ipynb
│   └── 04_advanced_models.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Data loading and preprocessing utilities
│   ├── features.py         # Feature engineering pipeline
│   ├── models/
│   │   ├── baseline.py     # Naive/baseline models
│   │   ├── linear.py       # Linear regression models
│   │   └── gradient_boost.py  # LightGBM / XGBoost models
│   └── evaluate.py         # Evaluation metrics (RMSLE)
│
├── submissions/            # Kaggle submission CSV files
├── reports/
│   └── figures/            # Charts and visualizations
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Dataset

| File | Description |
|------|-------------|
| `train.csv` | Training data with target `sales` |
| `test.csv` | Test data for submission |
| `stores.csv` | Store metadata (city, state, type, cluster) |
| `oil.csv` | Daily oil price (Ecuador is oil-dependent economy) |
| `holidays_events.csv` | National/regional/local holidays and events |
| `transactions.csv` | Number of transactions per store per day |

## 🧠 Models Explored

- [ ] Baseline (mean/last-value)
- [ ] Linear Regression with time features
- [ ] LightGBM
- [ ] XGBoost
- [ ] ARIMA / SARIMA
- [ ] Facebook Prophet
- [ ] Neural Networks (LSTM / Temporal Fusion Transformer)

## 📏 Evaluation Metric

Submissions are evaluated using **Root Mean Squared Logarithmic Error (RMSLE)**:

$$\text{RMSLE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} \left(\log(1 + \hat{y}_i) - \log(1 + y_i)\right)^2}$$

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/DinisMiranda/store-sales-forecasting.git
cd store-sales-forecasting
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Download the data
Download the competition data from [Kaggle](https://www.kaggle.com/competitions/store-sales-time-series-forecasting/data) and place it in the `data/raw/` directory.

```bash
kaggle competitions download -c store-sales-time-series-forecasting
unzip store-sales-time-series-forecasting.zip -d data/raw/
```

### 4. Start exploring
```bash
jupyter notebook notebooks/01_eda.ipynb
```

## 🔗 References

- [Kaggle Competition Page](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)
- [Corporación Favorita](https://en.wikipedia.org/wiki/Corporaci%C3%B3n_Favorita)
- [LightGBM Documentation](https://lightgbm.readthedocs.io/)
- [Facebook Prophet](https://facebook.github.io/prophet/)

---

> **Author:** Dinis Miranda · [GitHub](https://github.com/DinisMiranda)
