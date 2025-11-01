import pandas as pd
d = pd.read_csv("students.csv")

def predict(a, s, p):
    if a == "High" and s == "Long": return "Pass"
    elif a == "High" and p > 65: return "Pass"
    elif a == "Medium" and s in ["Long","Medium"] and p > 55: return "Pass"
    elif a == "Low" and s == "Short": return "Fail"
    elif p < 50: return "Fail"
    else: return "Fail"

print("Predictions:")
print("Student 1 ->", predict("Low", "Short", 35))
print("Student 2 ->", predict("High", "Long", 80))
print("Student 3 ->", predict("Medium", "Medium", 60))

c = 0
for i, r in d.iterrows():
    pred = predict(r['Attendance'], r['StudyTime'], r['PreviousScore'])
    if pred == r['Result']: c += 1
    print(f"S{i+1}: A={r['Result']}, P={pred}")
print("Accuracy:", round((c/len(d))*100,2), "%")
