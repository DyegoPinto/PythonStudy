# %%

# import of libraries

import os
import zipfile

# %%

# Variables 

source_dir  = 'C:/Users/dyego/PandasProject/Files'
destiny_dir = 'C:/Users/dyego/PandasProject/Sample/TSE'
# %%

for zip_files in os.listdir(source_dir):
    #print(zip_files)

    if (os.path.splitext(zip_files)[1]=='.zip'):
        print(zip_files)

        with zipfile.ZipFile(f'{source_dir}/{zip_files}','r') as zip_files:
            zip_files.extractall(path=destiny_dir)
# %%

