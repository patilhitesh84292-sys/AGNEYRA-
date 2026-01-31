# Student Result Prediction - Basic ML (Windows 7 Compatible)

import csv
import random

# Load dataset
dataset = []
with open('student_data.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        dataset.append({
            "Marks": float(row["Marks"]),
            "Attendance": float(row["Attendance"]),
            "Result": int(row["Result"])
        })

# Train/Test split (80/20)
random.shuffle(dataset)
split_index = int(0.8 * len(dataset))
train_data = dataset[:split_index]
test_data = dataset[split_index:]

# Simple logistic-like model using threshold
# Rule: Probability = (Marks/100 + Attendance/100)/2
# If probability >= 0.625 → PASS else FAIL

def predict(student):
    prob = (student["Marks"]/100 + student["Attendance"]/100)/2
    return 1 if prob >= 0.625 else 0

# Evaluate on test data
correct = 0
for s in test_data:
    if predict(s) == s["Result"]:
        correct += 1

accuracy = (correct / len(test_data)) * 100
print("Model Accuracy:", round(accuracy,2), "%")

# Input new student
marks = float(input("\nEnter marks of student (0-100): "))
attendance = float(input("Enter attendance % of student (0-100): "))

new_student = {"Marks": marks, "Attendance": attendance}
result = predict(new_student)

if result == 1:
    print("Prediction: PASS ✅")
else:
    print("Prediction: FAIL ❌")
