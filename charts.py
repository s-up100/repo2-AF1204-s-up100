import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
    "Attendance": [60,65,70,75,80,85,90,92,95,97],
    "Assignments": [2,3,4,5,6,7,8,9,9,10],
    "Sleep_Hours": [8,7,7,6,6,6,5,5,5,4],
    "Exam_Score": [50,55,60,65,70,75,80,85,88,92]
}

df = pd.DataFrame(data)

# Chart 1
sns.regplot(x="Hours_Studied", y="Exam_Score", data=df)
plt.savefig("chart1.png")
plt.clf()

# Chart 2
sns.scatterplot(x="Attendance", y="Exam_Score", data=df)
plt.savefig("chart2.png")
plt.clf()

# Chart 3
sns.histplot(df["Exam_Score"])
plt.savefig("chart3.png")
plt.clf()

# Chart 4
sns.boxplot(y=df["Exam_Score"])
plt.savefig("chart4.png")
plt.clf()

print("Charts created")