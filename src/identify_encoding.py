# %%

# import libraries

import pandas as pd
import user_libraries.libraries as lib


# %%

file = 'C:/Users/dyego/PandasProject/Sample/TSE/consulta_cand_2022_AC.csv'
encoding_detected = lib.find_encoding(file)
delimiter = lib.find_delimeter(file)

# read file 
df = pd.read_csv(file
                 ,encoding=encoding_detected
                 ,sep=delimiter)

df

# %%
