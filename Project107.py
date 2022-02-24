import csv
import pandas as pd
import plotly.express as px

df = pd.read_csv("Data.csv")
mean = df.groupby(["student_id","level"],as_index = False)["attempt"].mean()
#print(df.groupby("level")["attempt"].mean())
graph = px.scatter(mean,x="student_id",y="level",color="attempt",size="attempt")
graph.show()

