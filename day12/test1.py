import pandas as pd
drinks=pd.read_csv("Downloads/drinks.csv")
column_to_remove='beer_servings'
drinks=drinks.drop(column_to_remove,axis=1)
drinks.to_csv("drinks.csv",index=False)
drinks["servings"]=drinks["spirit_servings"]+drinks["wine_servings"]