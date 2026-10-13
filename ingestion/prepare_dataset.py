
from pathlib import Path
import pandas as pd

# Project root and input/output paths

ROOT = Path(__file__).resolve().parent.parent
input_file = ROOT / "data" / "Online Retail.xlsx"
output_file = ROOT / "data" / "sample_sales.csv"


if not input_file.exists():
    raise FileNotFoundError(
        f"Dataset not found: {input_file}"
    )

df = pd.read_excel(input_file, engine="openpyxl")

# Standardize column names for our pipeline
df = df.rename(columns={
    "InvoiceNo": "InvoiceNo",
    "StockCode": "StockCode",
    "Description": "Description",
    "Quantity": "Quantity",
    "InvoiceDate": "InvoiceDate",
    "UnitPrice": "UnitPrice",
    "CustomerID": "CustomerID",
    "Country": "Country"
})

df.to_csv(output_file, index=False)

print("Dataset converted successfully!")
print("Rows:", len(df))
print("Columns:", list(df.columns))
print("Saved to:", output_file)
