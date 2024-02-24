# %%

# import of libraries
import pandas as pd
#import numpy as np
from user_libraries.environment_setup import importa_arquivo_videos_youtube 

# display setup 
pd.options.display.max_rows = 999
pd.options.display.max_columns=999
pd.options.display.float_format = "{:.2f}".format

# %% 

# 99 - ENVIRONMENT SETUP

source_file = 'C:/Users/dyego/PandasProject/Files/videos/USvideos.csv'
destination_file = 'C:/Users/dyego/PandasProject/Files/videos/videos_youtube.csv'
param_json = "C:/Users/dyego/PandasProject/src/param/config.json"

importa_arquivo_videos_youtube(source_file
              , destination_file
              , param_json)


# %%

# 00 - FILE IMPORT - VIDEOS YOUTUBE

dfVideoYouTube = pd.read_csv(destination_file
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.info()
# %%

# select some columns

colunas = ['CodVideoYouTube','NomVideo']

dfVideoYouTube[colunas]

# %%

#command loc works with [index, columns], where : means all indexes

dfVideoYouTube.loc[:, colunas]

# %%

#select distinct values

#dfVideoYouTube['NomCanal'].unique()

#drop_duplicates will make a distinct of all the rows that have the same values in all of the columns
#dfVideoYouTube.drop_duplicates()

#dfVideoYouTube['NomCanal'].drop_duplicates()

#brings all the columns where the NomCanal has unique values
#dfVideoYouTube.drop_duplicates(subset=['NomCanal'])

#keep =
#False = values that never appeared more then one time
#'first'= eliminate the duplicates keeping the first occurrences
#'last'= eliminate the duplicates keeping the last occurrences

#dfVideoYouTube.drop_duplicates(subset=['NomCanal'], keep=False)

#dfVideoYouTube.drop_duplicates(subset=['NomCanal'], keep='first')

dfVideoYouTube.drop_duplicates(subset=['NomCanal'], keep='last').count()
# %%


dfVideoYouTube.head(5)

dfVideoYouTube.tail(5)

dfVideoYouTube.sample(5) #- 5 random

# %%

#verify all the numeric columns and bring some statistics
dfVideoYouTube.describe().T

#brings the statistics of just one column
dfVideoYouTube['NumVisualizacao'].describe()
# %%

# APPLYING THE FILTER CONDITION

dfVideoYouTube['NomCanal'] = dfVideoYouTube['NomCanal'].str.lower()

df_NomCanalQtd = dfVideoYouTube.groupby('NomCanal', as_index=False).agg(QTD=('NomCanal', 'count'))

#df_NomCanalQtd = dfVideoYouTube.groupby(dfVideoYouTube['NomCanal'].str.lower(), as_index=False).agg(QTD=('NumVisualizacao', 'count'))
# %%

df_NomCanalQtd.info()

# %%

qtd_equal_1 = df_NomCanalQtd['QTD']==1

#df_NomCanalQtd[qtd_equal_1]
df_NomCanalQtd.loc[qtd_equal_1, ['NomCanal']]
# %%

qtd_in_1_10 = (df_NomCanalQtd['QTD'] > 0) & (df_NomCanalQtd['QTD'] < 11)

df_NomCanalQtd.loc[qtd_in_1_10].sort_values(by='QTD')['NomCanal']
# %%

df_NomCanalQtd[df_NomCanalQtd['QTD'].isin([1,10])]
# %%

df_NomCanalQtd.query("QTD > 0 and QTD < 11").sort_values(by='QTD')
# %%

# ORDER BY ASC

dfVideoYouTube.sort_values(by='CodCategoriaVideo')
# %%

# ORDER BY DESc

#dfVideoYouTube.sort_values(by='CodCategoriaVideo', ascending=False)

(dfVideoYouTube[dfVideoYouTube['NomCanal']=='jordan wilson']
    .sort_values(by='NumVisualizacao'
                 , ascending=False
                 ))
# %%

dfVideoYouTube.query("NomCanal == 'jordan wilson' ").sort_values(by='NumVisualizacao')

# %%

dfVideoYouTube.shape

# %%

#how to use group by

(dfVideoYouTube.groupby(['NomCanal'])
        .agg(QtdVideos=('NomVideo','count'))
        .sort_values(by='QtdVideos'
                     , ascending=False))
# %%

(dfVideoYouTube
        .query("NomCanal == 'ESPN' ")
        .groupby(['NomCanal'])
        .agg(QtdVideos=('NomVideo','count')))

# %%

(dfVideoYouTube[dfVideoYouTube['NomCanal']=='ESPN']
    .groupby(['NomCanal'])
    .agg(QtdVideos=('NomVideo','count')))

# %%

dfVideoYouTube_AGG = (dfVideoYouTube.groupby(['NomCanal'])
        .agg(QtdVideos=('NomVideo','count'))
        .sort_values(by='QtdVideos'
                     , ascending=False))

# %%

dfVideoYouTube_AGG[dfVideoYouTube_AGG['QtdVideos'] > 10].head(3)

# %%

dfVideoYouTube_AGG.query('QtdVideos > 10').head(3)

# %%

(dfVideoYouTube.groupby(['NomCanal'], as_index=False)
    .agg(QtdVis_TOT=('NumVisualizacao', 'sum')
         ,QtdVis_MIN=('NumVisualizacao', 'min')
         ,QtdVis_MAX=('NumVisualizacao', 'max')
         ,QtdVis_AVG=('NumVisualizacao', 'mean')
         )
    .sort_values(by='QtdVis_TOT',ascending=False)     
    )