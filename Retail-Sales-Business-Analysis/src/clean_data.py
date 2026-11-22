from pathlib import Path
import pandas as pd

source = Path("data/retail_sales.csv")
target = Path("data/retail_sales_clean.csv")

if not source.exists():
    raise FileNotFoundError("Add data/retail_sales.csv; see data/README.md")
df = pd.read_csv(source)
print("Shape:", df.shape)
print("Missing values:\n", df.isna().sum())
print("Duplicate rows:", df.duplicated().sum())
# Starter step only. Inspect the schema before adding column-specific rules.
df = df.drop_duplicates()
df.to_csv(target, index=False)
print("Saved:", target)
