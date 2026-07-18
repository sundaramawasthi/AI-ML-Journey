# Matplotlib = Python library for turning data into charts (Data Visualization).
# Numbers in a table are hard for our brain to scan; a graph makes trends,
# comparisons, and outliers jump out instantly.
# Install once (only needed if it isn't already installed):
# !pip install matplotlib

import random

import pandas as pd
import matplotlib.pyplot as plt  # matplotlib -> library, pyplot -> plotting module, plt -> short alias

random.seed(42)  # fixes the "random" numbers below so the lesson looks the same every run

# AI/ML connection: before training a model we usually go
# Dataset -> Pandas (clean it) -> Matplotlib (visualize it) -> spot patterns -> Machine Learning.
# Visualizing data BEFORE modeling helps catch problems (outliers, imbalance, weird
# distributions) that are nearly invisible when just staring at rows and columns.


# ---------------------------------------------------------------------------
# 1. YOUR FIRST LINE CHART
# ---------------------------------------------------------------------------
# A line chart is best for showing how a value changes, e.g. over time.

x = [1, 2, 3, 4, 5]           # month number -> x-axis: input / independent variable
y = [120, 180, 150, 240, 310]  # website visitors -> y-axis: output / dependent variable

plt.figure()  # starts a fresh canvas so this chart doesn't draw on top of a previous one
plt.plot(x, y)
plt.title("First Line Chart: Website Visitors")
plt.xlabel("Month Number")
plt.ylabel("Visitors")
plt.show()
# Line charts are the go-to for stock prices, temperature, revenue, and
# tracking a model's accuracy/loss across training epochs.


# ---------------------------------------------------------------------------
# 2. CUSTOMIZING A CHART
# ---------------------------------------------------------------------------
# A bare chart works, but labels, color, and markers make it much easier to read.
plt.figure(figsize=(6, 4))  # figsize=(width, height) in inches

plt.plot(
    x,
    y,
    color='green',
    marker='s',       # 's' = square marker at every data point
    linestyle=':',     # dotted line
    linewidth=2,       # line thickness
    markersize=8       # marker size
)
plt.title("Monthly Website Visitors")
plt.xlabel("Month Number")
plt.ylabel("Visitors")
plt.show()
# Good visualizations are: easy to read -> clearly labelled -> easy to understand.


# ---------------------------------------------------------------------------
# 3. MULTIPLE LINES + LEGEND (comparing two datasets)
# ---------------------------------------------------------------------------
months = [1, 2, 3, 4, 5]
visitors_2025 = [100, 150, 190, 230, 270]
visitors_2026 = [130, 180, 220, 280, 340]

# label='...' names each line; plt.legend() then draws a key so you can
# tell the lines apart -> without it there's no way to know which line is which.
plt.figure()
plt.plot(months, visitors_2025, label='Visitors 2025')
plt.plot(months, visitors_2026, label='Visitors 2026')
plt.title("Year-on-Year Website Visitors")
plt.xlabel("Months")
plt.ylabel("Visitors")
plt.legend()
plt.show()
# Useful for: actual vs predicted values, training vs validation accuracy,
# revenue across years, multiple sensors/trends on one chart.


# ---------------------------------------------------------------------------
# 4. BAR CHART (comparing categories)
# ---------------------------------------------------------------------------
teams = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Omega']
projects = [18, 27, 35, 22, 31]

plt.figure()
plt.bar(teams, projects)  # bar height = value
plt.title("Projects Completed by Teams")
plt.xlabel("Teams")
plt.ylabel("Projects")
plt.show()
# Useful for: feature importance, class distribution, sales by region,
# comparing model performance across categories.


# ---------------------------------------------------------------------------
# 5. HISTOGRAM (distribution of numeric data)
# ---------------------------------------------------------------------------
# A histogram is NOT the same as a bar chart: a bar chart compares separate
# categories, a histogram groups a single numeric column into ranges (bins)
# and counts how many values fall in each range.
ages = [random.randint(18, 65) for _ in range(400)]

plt.figure()
plt.hist(ages, bins=12)  # bins -> how many groups the age range is split into
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
# In ML/EDA, histograms answer: are most values small or large? is the data
# roughly balanced or skewed? are there extreme outliers I should investigate?


# ---------------------------------------------------------------------------
# 6. PIE CHART (part-to-whole)
# ---------------------------------------------------------------------------
activities = ['Coding', 'Reading', 'Projects', 'Breaks', 'Other']
hours = [8, 5, 6, 3, 2]

plt.figure()
plt.pie(
    hours,
    labels=activities,
    autopct='%1.1f%%',  # show each slice's share as a percentage, e.g. "33.3%"
    startangle=90
)
plt.title("Daily Time Distribution")
plt.show()
# Good for class proportions, market share, dataset composition -
# but only when the number of categories is small; too many slices get unreadable.


# ---------------------------------------------------------------------------
# 7. SCATTER PLOT (relationship between two numeric variables)
# ---------------------------------------------------------------------------
study_hours = [1, 2, 3, 4, 5, 6]
exam_scores = [42, 51, 58, 68, 77, 89]

plt.figure()
plt.scatter(study_hours, exam_scores)
plt.title("Study Hours vs Exam Score")
plt.xlabel("Study Hours")
plt.ylabel("Exam Score")
plt.show()
# If the points trend upward, more study hours tend to go with higher scores -
# a possible positive relationship. This is exactly the kind of check you'd do
# on features like experience-vs-salary or house-size-vs-price before modeling.


# ---------------------------------------------------------------------------
# 8. SUBPLOTS (multiple charts in one figure)
# ---------------------------------------------------------------------------
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
orders = [45, 62, 58, 76, 91]

hours = [2, 3, 4, 5, 6]
scores = [48, 57, 65, 74, 86]

plt.figure(figsize=(10, 4))

# subplot(rows, columns, position) -> a 1-row-by-2-column grid, this is chart #1
plt.subplot(1, 2, 1)
plt.bar(days, orders)
plt.title("Daily Orders")
plt.xlabel("Weekdays")
plt.ylabel("Orders")

# same grid, this is chart #2
plt.subplot(1, 2, 2)
plt.scatter(hours, scores)
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")

plt.tight_layout()  # stops the two charts' titles/labels from overlapping
plt.show()
# Subplots are handy for side-by-side EDA, comparing experiment results, or
# putting multiple views of a model's evaluation in one figure.


# ---------------------------------------------------------------------------
# 9. MATPLOTLIB + PANDAS (the real Data Science workflow)
# ---------------------------------------------------------------------------
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'],
    'Revenue': [14500, 17200, 15800, 21300, 24900]
}
df = pd.DataFrame(data)
print(df)

# Matplotlib can plot columns straight out of a DataFrame - no need to
# convert them to plain lists first.
plt.figure()
plt.bar(df['Month'], df['Revenue'])
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()
# Workflow: CSV file -> pd.read_csv() -> clean with Pandas -> visualize with
# Matplotlib -> feed cleaned, understood data into a Machine Learning model.


# ---------------------------------------------------------------------------
# 10. SAVING A CHART AS AN IMAGE FILE
# ---------------------------------------------------------------------------
plt.figure()
plt.bar(df['Month'], df['Revenue'])
plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

# savefig() must be called BEFORE show() - show() can clear the figure
# afterwards, so saving first guarantees the file matches what you saw.
plt.savefig("monthly_revenue.png")
plt.show()
print("Chart saved as monthly_revenue.png")
# Other common formats: .jpg, .pdf, .svg - handy for reports, papers, dashboards,
# and slide decks where you need a static copy of the chart.


# ---------------------------------------------------------------------------
# WHAT'S NEXT: the object-oriented interface
# ---------------------------------------------------------------------------
# Everything above uses the quick "pyplot" style (plt.plot, plt.title, ...),
# which is great for fast, single charts. For more control - especially with
# many subplots - Matplotlib also offers an object-oriented interface built
# around explicit Figure and Axes objects:
#
#   fig, ax = plt.subplots()
#   ax.plot(x, y)
#   ax.set_title("Example")
#
# fig -> the whole image/canvas, ax -> one chart living inside it. That gives
# finer control over figure layout, multiple axes, and reusable plotting code.
