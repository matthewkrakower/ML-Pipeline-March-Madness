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

model = joblib.load("/opt/airflow/models/xgb_model.pkl")

preds = model.predict(X_test)

out = test_df.copy()
out["prediction"] = preds
out["Team"] = team_col['Team']
year = datetime.datetime.now().year
out.to_csv(f"/opt/airflow/results/predictions_{year}.csv", index=False)