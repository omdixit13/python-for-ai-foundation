import pandas as pd

data = {
    "Name": ["Om", "Aman", "Ravi"],
    "Score": [88, 92, 79]
}

df = pd.DataFrame(data)

print(df)
print("Average Score:", df["Score"].mean())
print("Max Score:", df["Score"].max())
