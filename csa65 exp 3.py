import pandas as pd

# Student dataset with missing values
data = {
    "Student": ["Asha", "Rahul", "Priya", "Kiran", "Meena"],
    "Marks": [85, 90, None, 78, None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Replace missing values with mean
mean_marks = df["Marks"].mean()
df["Marks"] = df["Marks"].fillna(mean_marks)

print("\nCleaned Dataset:")
print(df)

# Statistical Information
average_marks = df["Marks"].mean()
highest_score = df["Marks"].max()

print("\nStatistical Information")
print("Average Marks:", average_marks)
print("Highest Score:", highest_score)
