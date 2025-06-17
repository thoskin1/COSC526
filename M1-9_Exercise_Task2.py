import requests
import pandas as p
from io import StringIO

url = 'https://raw.githubusercontent.com/cosc-526/home.page/refs/heads/main/data.M.1.exercise.tsv'

response = requests.get(url)

if response.status_code == 200:
    file = p.read_csv(StringIO(response.text), delimiter='\t')
    
    rows = len(file)
    columns = file.shape[1]
    avg_age = float(file['age'].mean())
    
    print("Number of rows of data: ", rows)
    print("Number of cols: ", columns)
    print("Average Age: ", avg_age)