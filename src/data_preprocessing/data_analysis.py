# 📦 Imports
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 📥 Load Data
df = pd.read_csv("../data/processed/updated_data_with_points.csv")

# 📊 1. Summary Statistics
print("Summary of Assigned Points:")
print(df['Assigned Points'].describe())

plt.figure(figsize=(8, 4))
sns.histplot(df['Assigned Points'], bins=20, kde=True)
plt.title("Distribution of Assigned Points")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.show()

# 📈 2. Points Distribution by Difficulty Level
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Difficulty', y='Assigned Points')
plt.title("Points Distribution by Difficulty")
plt.show()

# 🔍 3. Missing Values Overview
print("\nMissing Values in Each Column:")
print(df.isnull().sum())

answered_ratio = df['Answer'].notnull().mean()
print(f"\nAnswer Rate: {answered_ratio:.2%}")
print(f"Missing Answer Rate: {(1 - answered_ratio):.2%}")

# 📚 4. Total Points Per Student
student_scores = df.groupby("Student_Id")["Assigned Points"].sum().reset_index()
student_scores.columns = ["Student_Id", "Total Score"]

print("\nTotal Score Statistics per Student:")
print(student_scores['Total Score'].describe())

plt.figure(figsize=(10, 4))
sns.histplot(student_scores["Total Score"], bins=20, kde=True)
plt.title("Total Score Distribution per Student")
plt.xlabel("Total Score")
plt.ylabel("Number of Students")
plt.show()

# 🏆 5. Top and Bottom Performing Students
print("\nTop 5 Students by Total Score:")
print(student_scores.sort_values(by="Total Score", ascending=False).head())

print("\nBottom 5 Students by Total Score:")
print(student_scores.sort_values(by="Total Score", ascending=True).head())

# 📉 6. Answer Rate by Difficulty Level
difficulty_answer_rate = df.groupby("Difficulty")["Answer"].apply(lambda x: x.notnull().mean()).reset_index()
difficulty_answer_rate.columns = ["Difficulty", "Answer Rate"]

print("\nAnswer Rate by Difficulty:")
print(difficulty_answer_rate)

plt.figure(figsize=(8, 4))
sns.barplot(data=difficulty_answer_rate, x="Difficulty", y="Answer Rate")
plt.title("Answer Rate by Question Difficulty")
plt.ylabel("Answer Rate")
plt.xlabel("Difficulty Level")
plt.ylim(0, 1)
plt.show()
