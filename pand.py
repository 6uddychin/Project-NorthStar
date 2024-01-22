import pandas as pd
import sys
import seaborn as sns
import json
import matplotlib.pyplot as plt



data = sys.argv[1]
df = pd.read_csv('month_row.csv')
# data = pd.read_json('visitsData.json')
# df = pd.read_json(data)
# df.to_json(orient='index')
# visit_df = df[['month','visits']]
print(df)
# df.to_csv('test_df.csv')
# d = json.loads(sys.argv[1])
print(type(df))
print(df)

sns.set_theme(style="white", palette=None)
sns.barplot(x='month',y='Company1', data=df, palette="rocket")
sns.despine(left=True, bottom=True)
plt.savefig("chart_noBorder.svg")
plt.show()
