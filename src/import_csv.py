# %%

#import of libraries
import pandas as pd
from glob import glob

# %%

# create dataframe to read the file

path = 'C:/Users/dyego/PandasProject/Files/consulta_cand_2022_AC.csv'

#print(path)

# by default the read_csv is utf-8 and the sep is comma
df = pd.read_csv(path
                 ,encoding='latin-1'
                 ,sep=';')

# %%

# visualize the dataframe 

#head() - return the first 5 rows by default
#tail() - return the last 5 rows by default
#sample() - return random rows when specificied. if not return 1 random row
df.sample(5)

df.info()
# %%

# create dataframe to read multiple files

path_all = 'C:/Users/dyego/PandasProject/Sample/TSE/consulta_cand_2022_*.csv'

files = sorted(glob(path_all))

dfFile = pd.DataFrame()

for data_to_import in files:
    
    df =  pd.read_csv(data_to_import
                 ,encoding='latin-1'
                 ,sep=';')
    
    dfFile = pd.concat([dfFile, df])

# %%

dfFile['SG_UF'].unique()
# %%
