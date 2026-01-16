import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from API
url = "http://127.0.0.1:5000/students"
response = requests.get(url)
data = response.json()

# Convert to DataFrame
df = pd.DataFrame(data)

subjects = [
    "math_score", "history_score", "physics_score",
    "chemistry_score", "biology_score", "english_score", "geography_score"
]

# Calculate average per student
df["average_score"] = df[subjects].mean(axis=1)

# Class average
class_average = df["average_score"].mean()
print("Class Average Score:", round(class_average, 2))

# Student full names
df["student_name"] = df["first_name"] + " " + df["last_name"]

# Bar chart
plt.figure(figsize=(10,6))
plt.bar(df["student_name"], df["average_score"])
plt.xticks(rotation=45, ha="right")
plt.xlabel("Students")
plt.ylabel("Average Score")
plt.title("Student Average Scores")
plt.tight_layout()
plt.show()