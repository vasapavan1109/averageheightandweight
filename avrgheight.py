import statistics
import pandas as pd
import plotly.express as plot_expres
df=pd.read_csv(r"C:\Users\rajuv\Desktop\python practice\SOCR-HeightWeight.csv")
h = df["Height"]
w = df["Weight"]

h_mean = statistics.mean(h)
print(h_mean)
w_mean = statistics.mean(w)
print(w_mean)

h_median = statistics.median(h)
print(h_mean)
w_median = statistics.median(w)
print(w_median)

h_mode = statistics.mode(h)
print(h_mean)
w_mode = statistics.mode(w)
print(w_mode)