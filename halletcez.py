import pandas as pd
import matplotlib.pyplot as plt 


df = pd.DataFrame(
    {
        "Name": [
            "Nazlican, Yalcin ",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
        ],
        "Age": [20, 35, 58],
        "Sex": ["female", "male", "female"],
    }
)


print(df)

df.to_excel("output.xlsx", index=False)

print(df["Age"])
ages = pd.Series([20, 35, 58], name="Age")

print(df.describe())

plt.hist(df["Age"], bins=5, color="skyblue", edgecolor="black")
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

