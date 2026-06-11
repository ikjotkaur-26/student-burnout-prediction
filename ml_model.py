#READ EXCLE FILE
import pandas as pd
df = pd.read_csv("student_datacsv.csv")
print(df.head())#ABOVE FIVE ROWS

# convert burnout in ml
df['Burnout']=df['Burnout'].map({
    'No':0,
    'Yes':1
})
print(df.head())

# train model in this part
X = df[
[
'Study_Hours',
'Sleep_Hours',
'Attendance',
'Stress_Level',
'Screen_Time',
'Assignments_Completed',
'Performance'
]
]

y = df['Burnout']

#train-test splits
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# CHECK SPLIT DONE OE NOT?
print("Training Data:", len(X_train))
print("Testing Data:", len(X_test))


# START MODEL BUILDING
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
print("MODEL TRAINED SUCCESSFULLY")

prediction = model.predict(X_test)

# ACCURACY TEST
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test , prediction)
print("Accuracy:" , accuracy)

# RE-CHECK
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, X, y, cv=5)
print("Final Accuracy:", scores.mean())

# CLASSIFICATION REPORT
from sklearn.metrics import classification_report
print("Classification Report")
print(classification_report(y_test, prediction))

# CONFUSION MATRIX
from sklearn.metrics import confusion_matrix
print("CONFUSION MATRIX")
print(confusion_matrix(y_test, prediction))
# 6 NO BURNOUT, 4 BURNOUT