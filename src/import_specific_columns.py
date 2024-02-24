# %%

# import of libraries
import pandas as pd

# %%

# variables

source_file = 'C:/Users/dyego/PandasProject/Files/precos-gasolina-etanol-06.csv'
encoding = 'UTF-8'
sep= ';'
header= 0
destination_file = 'C:/Users/dyego/PandasProject/Files/precos_combustiveis.csv'
cols_index = 1,2,8,10,11,12
cols_name = ['UF','Municipio','Bairro','Produto','DataColeta','ValorVenda']
dtype = {
    'UF'            : 'string'
    ,'Municipio'    : 'string'
    ,'Bairro'       : 'string'
    ,'Produto'      : 'string'
    #,'DataColeta'   : 'string'
    ,'ValorVenda'   : 'string'
}

df = pd.read_csv(source_file
                 ,sep=sep
                 ,encoding=encoding
                 ,usecols=cols_index
                 ,names=cols_name
                 ,parse_dates=['DataColeta']
                 ,dayfirst=True
                 ,dtype=dtype
                 ,header=header)
# %%
df['ValorVenda'] = df['ValorVenda'].str.replace(',','.').astype(float)

df.info()
# %%

# generating the final file

df.to_csv(destination_file
          ,sep=sep
          ,index=False)

# %%
