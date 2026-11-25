"""Analyze college mess food waste using sample CSV data."""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "mess_food_waste_sample.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["date"])
required = {"date", "meal", "students_served", "food_prepared_kg", "food_waste_kg"}
missing = required - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {sorted(missing)}")
if (df[["students_served", "food_prepared_kg", "food_waste_kg"]] < 0).any().any():
    raise ValueError("Counts and food weights must be non-negative.")

df["waste_percent"] = (df["food_waste_kg"] / df["food_prepared_kg"] * 100).round(2)
summary = df.groupby("meal", as_index=False).agg(
    total_waste_kg=("food_waste_kg", "sum"),
    average_waste_kg=("food_waste_kg", "mean"),
    average_waste_percent=("waste_percent", "mean"),
    average_students=("students_served", "mean"),
)
summary.to_csv(OUT / "meal_summary.csv", index=False)

daily = df.groupby("date", as_index=False)["food_waste_kg"].sum()
daily.to_csv(OUT / "daily_summary.csv", index=False)

# Chart 1: total waste by meal
plt.figure(figsize=(8, 4.8))
plt.bar(summary["meal"], summary["total_waste_kg"])
plt.title("Total Food Waste by Meal")
plt.xlabel("Meal")
plt.ylabel("Food waste (kg)")
plt.tight_layout()
plt.savefig(OUT / "waste_by_meal.png", dpi=160)
plt.close()

# Chart 2: daily waste trend
plt.figure(figsize=(9, 4.8))
plt.plot(daily["date"], daily["food_waste_kg"], marker="o", markersize=3)
plt.title("Daily Food Waste Trend")
plt.xlabel("Date")
plt.ylabel("Food waste (kg)")
plt.xticks(rotation=35)
plt.tight_layout()
plt.savefig(OUT / "daily_waste_trend.png", dpi=160)
plt.close()

# Chart 3: average waste percentage by meal
plt.figure(figsize=(8, 4.8))
plt.bar(summary["meal"], summary["average_waste_percent"])
plt.title("Average Waste as % of Prepared Food")
plt.xlabel("Meal")
plt.ylabel("Waste (%)")
plt.tight_layout()
plt.savefig(OUT / "waste_percent_by_meal.png", dpi=160)
plt.close()

print("Analysis complete. Summary tables and charts are in the outputs/ folder.")
print(summary.to_string(index=False))
