import pandas as pd
import joblib
import os

os.makedirs("artifacts", exist_ok=True)

test_df = pd.read_csv("data/mmkp_preprocessed_test.csv")

X_test = test_df.drop(columns=['Winner', 'Team', 'ORtgSOS Rank', 'Losses', 'DRtgSOS Rank',
             'Luck Rank', 'NetRtgSOS Rank', 'NetRtg Rank', 'DRtg Rank',
             'ORtgSOS', 'ORtg Rank', 'DRtgSOS', 'Tourney Seed', 'AdjT Rank',
             'NetRtgSOSNC', 'ORtg', 'NetRtgSOS', 'AdjT', 'Luck',
             'NetRtgSOSNC Rank', 'Year'], errors="ignore")

model = joblib.load("artifacts/xgb_model.pkl")

preds = model.predict(X_test)

out = test_df.copy()
out["prediction"] = preds
out.to_csv("results/predictions.csv", index=False)