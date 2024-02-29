import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv('country_indicators.csv')

medval=str(df['Value'].median())

print(medval)

df['Value'] =df['Value'].replace(np.nan,medval)
df['Value'] = df['Value'].astype(float)

print(df)

df2 = df.groupby("Country Name",as_index=False)["Value"].max()

print(df2)

df2.to_csv("CI2",encoding='utf-8')

fig1=px.bar(df2,x='Country Name',y='Value',barmode='stack',title='Max Value for each Country')

fig1.show()

#print(df) 