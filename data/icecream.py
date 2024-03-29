import plotly.express as px
import csv

with open("Ice-Cream vs Cold-Drink vs Temperature - Ice Cream Sale vs Temperature data.csv") as csv_file:
      df = csv.DictReader(csv_file)
      fig = px.scatter(df,x="Temperature", y="Ice-cream Sales( ₹ )",z="Cold drink sales( ₹ )")
      fig.show()
