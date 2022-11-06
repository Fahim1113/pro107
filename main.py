import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
#names
arr1 = []
#levels
arr2 = []
#attempt
arr3 = []

for i in list(df["student_id"]):
  a = i in arr1
  if a == False:
    arr1.append(i)
    arr1.append(i)
    arr1.append(i)
    arr1.append(i)
    arr2.append("level1")
    arr2.append("level2")
    arr2.append("level3")
    arr2.append("level4")
    studentDF = df.loc[df["student_id"] == i]

    if studentDF.loc[studentDF["level"] == "Level 1"].empty:
      l1 = 0
      x1 = [0]
    else:
      l1 = studentDF.loc[studentDF["level"] == "Level 1"]
      x1 = l1.groupby("level")["attempt"].mean()
    
    if studentDF.loc[studentDF["level"] == "Level 2"].empty:
      l2 = 0
      x2 = [0]
    else:
      l2 = studentDF.loc[studentDF["level"] == "Level 2"]
      x2 = l2.groupby("level")["attempt"].mean()
    
    if studentDF.loc[studentDF["level"] == "Level 2"].empty:
      l3 = 0
      x3 = [0]
    else:
      l3 = studentDF.loc[studentDF["level"] == "Level 3"]
      x3 = l3.groupby("level")["attempt"].mean()
    
    if studentDF.loc[studentDF["level"] == "Level 4"].empty:
      l4 = 0
      x4 = [0]
    else:
      l4 = studentDF.loc[studentDF["level"] == "Level 4"]
      x4 = l4.groupby("level")["attempt"].mean()
    arr3.append(x1[0])
    arr3.append(x2[0])
    arr3.append(x3[0])
    arr3.append(x4[0])

df2 = pd.DataFrame({
  "student":arr1,
  "level":arr2,
  "attempt":arr3,
})

fig = px.scatter(
    data_frame=df2,
    x="student",
    y="level",
    color="attempt",
    size="attempt"
)
fig.show()