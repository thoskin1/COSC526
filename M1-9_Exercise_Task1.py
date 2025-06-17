import requests
import pandas as p
from io import StringIO

url = 'https://raw.githubusercontent.com/cosc-526/home.page/1faf96d496a05b129c3f6a5844d2d490027a92a5/data.M.1.exercise.csv'

response = requests.get(url)

if response.status_code == 200:
    file = p.read_csv(StringIO(response.text))
    
    rows = len(file)
    columns = file.shape[1]
    avg_age = float(file['age'].mean())
    
    print("Number of rows of data: ", rows)
    print("Number of cols: ", columns)
    print("Average Age: ", avg_age)