import papermill as pm
import os

for dataset in os.listdir("datasets"):
   truncated_name = dataset.split(".")[0]
   os.makedirs("outputs/" + truncated_name)
   pm.execute_notebook(
      'StockPrediction.ipynb',
      'executed_notebooks/' + truncated_name + '.ipynb',
      parameters=dict(file_path=dataset)
   )