import pandas as pd
import numpy

data= pd.read_csv("manga.csv")
titles = data[['title', 'title_en']]
print(titles)
titles.to_csv('titles.csv', index=False)
