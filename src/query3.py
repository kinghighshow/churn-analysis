import pandas as pd

df = pd.read_csv("data/churn_dataset.csv")

male_fiber_customers = df[
    (df["gender"] == "Male") &
    (df["InternetService"] == "Fiber optic")
]

print(male_fiber_customers)
print(f"Total male Fiber optic customers: {len(male_fiber_customers)}")