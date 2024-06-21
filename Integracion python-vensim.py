import venpy
import pandas as pd

model = venpy.Model('C:\Users\illan\Downloads\GLOBAL.mdl')
model.run_simulation('GLOBAL')

results = model.export_results('results.csv')
results_df= pd.read_csv('results.csv')
print(results_df)