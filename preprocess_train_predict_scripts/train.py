from sklearn.model_selection import RepeatedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import ElasticNet
from xgboost import XGBRegressor
import joblib


mmkp = pd.read_csv("data/mmkp_preprocessed_train.csv")

X = mmkp.drop(columns=['Winner', 'Team', 'ORtgSOS Rank', 'Losses', 'DRtgSOS Rank', 
                        'Luck Rank', 'NetRtgSOS Rank', 'NetRtg Rank', 'DRtg Rank',
                        'ORtgSOS', 'ORtg Rank', 'DRtgSOS', 'Tourney Seed', 'AdjT Rank',
                        'NetRtgSOSNC', 'ORtg', 'NetRtgSOS', 'AdjT', 'Luck', 
                        'NetRtgSOSNC Rank', 'Year'])
y = mmkp['Winner']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X) 

param_grid = {
    'n_estimators': [100, 200, 300],
    'max_depth': [3, 5, 7, 10],
    'learning_rate': [0.01, 0.05, 0.1],
    'subsample': [0.6, 0.8, 1.0],
    'colsample_bytree': [0.6, 0.8, 1.0],
    'gamma': [0, 1, 5],
    'reg_alpha': [0, 0.1, 1],
    'reg_lambda': [1, 1.5, 2]
}

grid = RandomizedSearchCV(
    estimator=XGBRegressor(random_state=0, objective='reg:squarederror'),
    param_distributions=param_grid,
    n_iter=30,    
    cv=5,
    scoring='neg_mean_squared_error',
    random_state=0,
    verbose=1,       
    n_jobs=-1                       
)
grid.fit(X_scaled, y)
xgb_best_params = grid.best_params_
print("Best Parameters:", xgb_best_params)

rkf = RepeatedKFold(n_splits=5, n_repeats=10, random_state=0)
mse_scores = []
mae_scores = []
rmse_scores = []
r2_scores = []

for train_idx, val_idx in rkf.split(X):
    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    X_train_scaled = X_train
    X_val_scaled = X_val

    model = XGBRegressor(**xgb_best_params, random_state=0, objective='reg:squarederror')
    model.fit(X_train_scaled, y_train)
    preds = model.predict(X_val_scaled)

    mse_scores.append(mean_squared_error(y_val, preds))
    mae_scores.append(mean_absolute_error(y_val, preds))
    rmse_scores.append(np.sqrt(mean_squared_error(y_val, preds)))
    r2_scores.append(r2_score(y_val, preds))

print(f"Mean MSE: {np.mean(mse_scores):.6f} with Std of {np.std(mse_scores):.6f}")
print(f"Mean MAE: {np.mean(mae_scores):.6f}")
print(f"Mean RMSE: {np.mean(rmse_scores):.6f}")
print(f"Mean R²: {np.mean(r2_scores):.6f}")

#Why the Mean is Trustworthy in This Case:
#1.	RKF already reduces variance by averaging across multiple shuffled train/test splits, unlike a single K-Fold split which may be biased depending on the fold.
#2.	A low std means stability: Your model’s performance doesn’t vary much across splits. So, the mean MSE is capturing a consistent performance signal — not one driven by outliers or unlucky folds.
#3.	Cross-validation mean approximates true error: With enough folds and repeats, the mean MSE approximates how your model would perform on unseen data.

joblib.dump(model, "/models/xgb_model.pkl")

loaded_model = joblib.load("/models/xgb_model.pkl")

preds_loaded = loaded_model.predict(X_scaled)