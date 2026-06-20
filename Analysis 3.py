import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Palak\Downloads\responses.csv.csv")
print(list(df.columns))
question = df.columns[3]
x = df[question]
count = x.value_counts()
plt.title("People aware what antiobiotics work against")
plt.xlabel("Antibiotics work against")
plt.ylabel("Count")
counts_index = count.index
counts_values = count.values
plt.bar(
    counts_index,
    counts_values,
    hatch="//",
    color=["g", "r", "b", "y"],
    edgecolor="blue",
)
plt.show()
