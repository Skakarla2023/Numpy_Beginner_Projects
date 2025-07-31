import numpy as np

data = np.array([
    [110, 120, 80, 190, 24.5],
    [145, 135, 85, 220, 29.1],
    [95, 115, 75, 180, 22.0],
    [160, 145, 95, 240, 33.4],
    [130, 130, 90, 210, 27.8]
])

columns = ["Glucose", "Systolic_BP", "Diastolic_BP", "Cholestrol", "BMI"]
patients = ["Patient 1", "Patient 2", "Patient 3", "Patient 4","Patient 5"]

print(f"\nAverage Values:\n")
for i,col in enumerate(columns):
  print(f"{col}:{np.mean(data[:,i]):.2f}")

high_sugar = data[:,0]>140
high_bp=(data[:,1]>130)|(data[:,2]>90)
high_cholestrol=data[:,3]>300
high_BMI=data[:,4]>30

print("Patient Assessments:")
for i in range(len(data)):

  print(f"\n{patients[i]}:")
  if high_sugar[i]:
    print("High Blood sugar")
  if high_bp[i]:
    print("High Blood pressure")
  if high_cholestrol[i]:
    print("High cholestrol")
  if high_BMI[i]:
    print("High BMI")
  if not (high_sugar[i] or high_bp[i] or high_cholestrol[i] or high_BMI[i]):
    print("Person is healthy")


# using random values

import numpy as np
np.random.seed(42)
patients = ["patient 1", "patient 2, 'patient 3"]
days = 7
slots_per_day = 6

heart_rate = np.random.randint(60, 100, (3, 7, 6))
temperature = np.random.normal(36.5,0.5,(3, 6, 7))
systolic_bp = np.random.randint(100,140,(3, 6, 7))
diastolic_bp = np.random.randint(60, 90, (3, 6, 7))
sugar_level = np.random.randint(70, 180, (3, 6, 7))

def average_weekly_stats(parameter, name):
  for i,patient in enumerate(patients):
    avg = np.mean(parameter[i])
    print(f"{patient}:-Avg{name}:{avg:.2f}")


average_weekly_stats(heart_rate, "Heart Rate")
average_weekly_stats(temperature, "Temperature")
average_weekly_stats(systolic_bp, "Systolic BP")
average_weekly_stats(diastolic_bp, "Diastolic BP")
average_weekly_stats(sugar_level, "Sugar Level")
