# %%

# import of libraries
import pandas as pd
import numpy as np
from user_libraries.environment_setup import importa_arquivo_videos_youtube 

# display setup 
pd.options.display.max_rows = 999
pd.options.display.max_columns=999
pd.options.display.float_format = "{:.2f}".format

# %% 

# 99 - ENVIRONMENT SETUP

source_file = 'C:/Users/dyego/PythonProject/PythonStudy/PythonStudy/Files/videos/USvideos.csv'
destination_file = 'C:/Users/dyego/PythonProject/PythonStudy/PythonStudy/Files/videos/videos_youtube.csv'
param_json = "C:/Users/dyego/PythonProject/PythonStudy/PythonStudy/src/param/config.json"

#importa_arquivo_videos_youtube(source_file
#              , destination_file
#              , param_json)


# %%

# 00 - FILE IMPORT - VIDEOS YOUTUBE

dfVideoYouTube = pd.read_csv(destination_file
                 ,sep=';'
                 ,header=0)

dfVideoYouTube.info()
# %%


df_grouped = dfVideoYouTube.groupby(['NomCanal'], as_index=False).agg(NumVisualizacao=('NumVisualizacao','sum'))
# %%

df_grouped = df_grouped.query('NumVisualizacao > 1000000000')


# %%

df_new_info = pd.DataFrame({'NomCanal': ['new_row','new_row2']
                            ,'NumVisualizacao': [12327,232323]})

df_new_info
# %%

df_grouped = pd.concat([df_grouped, df_new_info],ignore_index=True)

# %%

df_grouped.query('NomCanal == "new_row"')
# %%

# DELETE 01 - NOT OPTIMIZED


#df_grouped = df_grouped.drop(labels=[13])

#we need to consult first, and then pass the index we want to remove
#df_grouped.drop(labels=[13], inplace=True)


df_grouped
# %%

# DELETE 02 - OPTIMIZED1

delete_condition = np.where(df_grouped['NomCanal'] == 'ibighit')[0]

df_grouped.drop(delete_condition, inplace=True)
# %%
