import pandas as pd
import numpy as np
import sys
df = pd.read_csv(sys.argv[1]+'/'+'flights.csv')

print( df )

df.to_csv(sys.argv[2]+'/'+'output.csv')
