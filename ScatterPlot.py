import pandas as pd
import plotly.express as pe

df = pd.read_csv("data.csv")
diagram = pe.scatter(df,x = "date", y = "cases", color = "country", title = "Covid cases in countries")
diagram.show()