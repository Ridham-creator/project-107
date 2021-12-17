import plotly.express as px
import csv
import numpy as np
import pandas as pd

df=pd.read_csv("datapro107.csv")
mean = df.groupby(["student_id", "level"], as_index=False)["attempt"].mean()
fig=px.scatter(mean,x="student_id", y="level", size="attempt",color="attempt")
fig.show()
