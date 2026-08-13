import pandas as pd
import numpy as np

marks = pd.Series([76,76,98], index=["math","science","english"])
print(marks["math"])
print(marks[["math","english"]])
