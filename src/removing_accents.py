# %%

# import of libraries

import pandas as pd
import user_libraries.libraries as lib
# %%

# variables
string_to_remove = 'étá'
result = ''

result = lib.remove_accents(string_to_remove)

print (result)


# %%

# reading a file with pandas

file = 'C:/Users/dyego/PandasProject/Files/accents.csv'

df = pd.read_csv(file
                 ,sep=';')

df
# %%
for i in df.index:
    df.loc[i, 'Aluno'] = lib.remove_accents(df.loc[i, 'Aluno'])  

df
# %%

for list in df['Aluno']:
    print (list)
    #df.loc[i, 'Aluno'] = lib.remove_accents(df.loc[i, 'Aluno'])  

#df

# %%
