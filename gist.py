import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Read the data from CSV files
path = os.path.abspath("/home/skull32/Modeling/data/random.txt")
data_df = pd.read_csv(path)
sequence = data_df["values"]

path1 = os.path.abspath("/home/skull32/Modeling/data/data.csv")
data_df1 = pd.read_csv(path1)
sequence1 = data_df1["values"]

# Create a single histogram for both sequences
plt.hist([sequence, sequence1], bins=20, edgecolor="black", alpha=0.5, label=["Сгенерированная ЧП", "Заданная ЧП"], stacked=False)


# Add titles and labels
plt.title("Сравнение гистограмм")
plt.xlabel("Значение")
plt.ylabel("Плотность")
plt.legend()
plt.grid(True)

# Display the histogram
plt.tight_layout()
plt.show()
