# %%

#first we need to install the yfinance and pandas_datareader

#pip install yfinance
#pip install pandas_datareader


# %%

# import libraries

import pandas as pd
import pandas_datareader.data as web
import yfinance as yf
yf.pdr_override()
from datetime import datetime

# %%

# Variables Scope
asset_name = 'PETR4.SA'
start_date = '2022-01-01'
end_date = '2023-01-01'
delivery_path = 'C:/Users/dyego/PandasProject/assets/'
file = 'petrobras.csv'
full_path = delivery_path+file


# %%

# Main code - Extraction process

df_Yfinance = web.get_data_yahoo(asset_name,start_date,end_date)

df_Yfinance = df_Yfinance.reset_index()

df_Yfinance.to_csv(full_path
                   ,sep=';'
                   ,index=False)

# %%

#assets_list = {'Asset': ['PETR4.SA', '^MERV']}
#dfAssets = pd.DataFrame(assets_list)

assets_list = 'C:/Users/dyego/PandasProject/assets/assets_param.csv'
fileUnified = 'unified.csv'
dateExtraction = datetime.now()

def api_yahoo_extraction(assets_list,delivery_path,file,start_date,end_date):  

    dfAssetsParam = pd.read_csv(assets_list)

    dfAll = pd.DataFrame()

    for asset_name in dfAssetsParam['Asset']:
        df_Yfinance = web.get_data_yahoo(asset_name,start_date,end_date)

        df_Yfinance = df_Yfinance.reset_index()

        #df_Yfinance.insert(0,'Asset', asset_name, True)

        #df_Yfinance['ExtractionDate'] = dateExtraction

        df_Yfinance = df_Yfinance.assign(ExtractionDate= dateExtraction
                                         ,AssetName= asset_name)

        dfAll = pd.concat([dfAll, df_Yfinance])

    full_path = delivery_path + file

    dfAll.to_csv(full_path
                    ,sep=';'
                    ,index=False)

# %%

api_yahoo_extraction(assets_list,delivery_path,fileUnified,start_date,end_date)

# %%

dfAssetsAll = pd.read_csv(delivery_path+fileUnified
                          ,sep=';'
                          ,parse_dates=['Date','ExtractionDate'])

dfAssetsAll = dfAssetsAll.assign(YEAR=dfAssetsAll['Date'].dt.year
                   ,MONTH=dfAssetsAll['Date'].dt.strftime('%m')
                   ,DAY=dfAssetsAll['Date'].dt.strftime('%d')
                   ,YEARMONTH=dfAssetsAll['Date'].dt.strftime('%Y-%m'))

dfAssetsAll = dfAssetsAll.rename(columns={
                        'Date' : 'NEGOTIATION_DATE'
})

dfAssetsAll = dfAssetsAll[['AssetName',
                           'NEGOTIATION_DATE',
                           'YEAR',
                           'MONTH',
                           'DAY',
                           'YEARMONTH',
                           'Open',
                           'High',
                           'Low',
                           'Close',
                           'Adj Close',
                           'Volume',
                           'ExtractionDate'
                           ]]

dfAssetsAll.to_csv(full_path
                    ,sep=';'
                    ,index=False)
# %%
