import pandas as pd
import glob

files = [item for item in glob.glob(r'*{}'.format('.py'))]  # glob(r'/home/vladimir/*{}'.format.....
print(files)

files = pd.read_excel(r'test.xlsx', skiprows=1)
# # Пропустили первую строку
# print(files)

print(files)
