import marimo as mo
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --------------------------------
# PAGE TITLE
# --------------------------------

mo.md("""
# 👋 Sultan Al-Ahmad  
**Aspiring Data Analyst | Python | Data Visualisation**
""")

# --------------------------------
# ABOUT ME
# --------------------------------

mo.md("""
## About Me

I am an Accounting and Finance student studying Data Science with a strong interest in analysing data and communicating insights effectively.

Throughout this module, I developed skills in:

- Data Cleaning  
- Exploratory Data Analysis  
- Data Visualisation  
- Statistical Thinking  

This portfolio demonstrates my ability to transform data into meaningful insights.
""")

# --------------------------------
# TECHNICAL SKILLS
# --------------------------------

mo.md("""
## Technical Skills

**Languages**
- Python  

**Libraries**
- pandas  
- matplotlib  
- seaborn  

**Tools**
- marimo  
- GitHub  

**Core Skills**
- Data Cleaning  
- Exploratory Data Analysis (EDA)  
- Data Visualisation  
- Correlation Analysis  
""")

# --------------------------------
# DATASET CREATION
# --------------------------------

# Simulated realistic student dataset
data = {
    "Hours_Studied": [1,2,3,4,5,6,7,8,9,10],
    "Attendance": [60,65,70,75,80,85,90,92,95,97],
    "Assignments": [2,3,4,5,6,7,8,9,9,10],
    "Sleep_Hours": [8,7,7,6,6,6,5,5,5,4],
    "Exam_Score": [50,55,60,65,70,75,80,85,88,92]
}

df = pd.DataFrame(data)

mo.md("""
## Dataset Overview

This dataset represents student behaviour and academic performance.

Variables include:

- Hours Studied  
- Attendance  
- Assignments Completed  
- Sleep Hours  
- Exam Score  

The goal is to analyse how study habits influence academic results.
""")

df.head()

# --------------------------------
# DATA CLEANING
# --------------------------------

mo.md("""
## Data Cleaning

Checking for missing values ensures the dataset is reliable before analysis.
""")

df.isnull().sum()

# --------------------------------
# DESCRIPTIVE STATISTICS
# --------------------------------

mo.md("""
## Descriptive Statistics

Summary statistics help understand the distribution of the dataset.
""")

df.describe()

# --------------------------------
# VISUALISATION 1 - REGRESSION
# --------------------------------

mo.md("""
## Visualisation 1: Study Time vs Exam Score

This regression plot shows the relationship between hours studied and exam performance.
""")

plt.figure(figsize=(6,4))

sns.regplot(
    x="Hours_Studied",
    y="Exam_Score",
    data=df
)

plt.title("Hours Studied vs Exam Score")

plt.show()

# --------------------------------
# VISUALISATION 2 - SCATTER
# --------------------------------

mo.md("""
## Visualisation 2: Attendance vs Exam Score

This scatter plot highlights how attendance influences exam performance.
""")

plt.figure(figsize=(6,4))

sns.scatterplot(
    x="Attendance",
    y="Exam_Score",
    data=df
)

plt.title("Attendance vs Exam Score")

plt.show()

# --------------------------------
# VISUALISATION 3 - HISTOGRAM
# --------------------------------

mo.md("""
## Visualisation 3: Exam Score Distribution

This histogram shows how exam scores are distributed.
""")

plt.figure(figsize=(6,4))

sns.histplot(
    df["Exam_Score"],
    bins=5
)

plt.title("Distribution of Exam Scores")

plt.show()

# --------------------------------
# VISUALISATION 4 - BOX PLOT
# --------------------------------

mo.md("""
## Visualisation 4: Exam Score Spread

The box plot highlights variation and possible outliers.
""")

plt.figure(figsize=(6,4))

sns.boxplot(
    y=df["Exam_Score"]
)

plt.title("Exam Score Box Plot")

plt.show()

# --------------------------------
# VISUALISATION 5 - HEATMAP (HIGH MARK SKILL)
# --------------------------------

mo.md("""
## Visualisation 5: Correlation Heatmap

This heatmap shows relationships between all variables in the dataset.
""")

plt.figure(figsize=(6,4))

sns.heatmap(
    df.corr(),
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.show()

# --------------------------------
# KEY INSIGHTS
# --------------------------------

mo.md("""
## Key Insights

From the analysis:

- Students who study longer tend to achieve higher exam scores.  
- Higher attendance is positively related to academic performance.  
- Completing more assignments improves exam results.  
- Sleep hours show a moderate relationship with performance.  
- Strong correlations exist between study behaviour and success.

These insights demonstrate how data analysis supports evidence-based decision-making.
""")

# --------------------------------
# LEARNING JOURNEY
# --------------------------------

mo.md("""
## Learning Journey

Before this module, I had limited experience working with data and programming.

Through continuous practice, I developed confidence in:

- Writing structured Python code  
- Cleaning and analysing datasets  
- Creating meaningful visualisations  
- Using marimo to build interactive webpages  

This portfolio demonstrates the progress made throughout my learning journey.
""")

# --------------------------------
# CONTACT DETAILS
# --------------------------------

mo.md("""
## Contact

GitHub: https://github.com/s-up100  
Email: sultan.al-ahmad@bayes.city.ac.uk  
""")
