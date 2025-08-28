import pandas as pd
import joblib
import os
from sklearn.preprocessing import StandardScaler
import datetime 


os.makedirs("artifacts", exist_ok=True)

test_df = pd.read_csv("/opt/airflow/data/mmkp_preprocessed_test.csv")
team_col = pd.read_csv("/opt/airflow/data/mmkp_test_team_col.csv")

X_test = test_df.drop(columns=['Winner'], errors="ignore")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_test) 

year = datetime.datetime.now().year

model = joblib.load(f"/opt/airflow/models/xgb_model_{year}.pkl")

preds = model.predict(X_test)

out = test_df.copy()
out["prediction"] = preds
out["Team"] = team_col['Team']
out.to_csv(f"/opt/airflow/results/predictions_{year}.csv", index=False)