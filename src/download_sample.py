# %%

#import of libraries OS - 

import os 
import requests
# %%

# Main Code - Download of 2 data sources

link = ['https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2022.zip'
       , 'https://www.ispdados.rj.gov.br/Arquivos/BaseDPEvolucaoMensalCisp.csv']

# Craetion of the directory
directory = 'C:/Users/dyego/PandasProject/Files'
file_name = 'NoneExistent'

os.makedirs(directory,exist_ok=True)

# %%

# Main code - execute the donwload process

for path in link:
    if path.__contains__('consulta_cand'):
        file_name = 'consulta_cand_2022.zip'
    elif path.__contains__('BaseDPEvolucaoMensalCisp'):
        file_name = 'BaseDPEvolucaoMensalCisp.csv'

    directory_delivery = f'{directory}/{file_name}'  

    print(path)
    print(file_name)
    print(directory_delivery)

    response = requests.get(path)

    with open(directory_delivery, 'wb') as download:
        download.write(response.content)


# %%
        
# Main Code - Download of 2 data sources

link = 'https://github.com/dbaassists/YouTube/blob/main/ArquivoDados/trips_data_new.csv'

# Craetion of the directory
directory = 'C:/Users/dyego/PythonProject/PythonStudy/PythonStudy/Files/UBER'
file_name = 'NoneExistent'

os.makedirs(directory,exist_ok=True)
# %%

response = requests.get(link)

file_name = 'trips_data_new.csv'

directory_delivery = f'{directory}/{file_name}'  

with open(directory_delivery, 'wb') as download:
    download.write(response.content)

# %%
