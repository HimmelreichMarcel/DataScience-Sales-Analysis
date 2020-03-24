import pandas as pd
import matplotlib.pyplot as plt
import os


def MergeData(files, path):
    all_data = pd.DataFrame()
    for file in files:
        current_data = pd.read_csv(path + "/" + file)
        all_data = pd.concat([all_data, current_data])
    return all_data


def CleanData(dataframe):
    # Find NAN
    nan_df = dataframe[dataframe.isna().any(axis=1)]

    all_data = dataframe.dropna(how='all')
    all_data.head()

    all_data = all_data[all_data['Order Date'].str[0:2] != 'Or']

    all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
    all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])


def GetCity(address):
    return address.split(",")[1].strip(" ")


def GetState(address):
    return address.split(",")[2].split(" ")[1]


def PreprocessData(dataframe):
    dataframe['Month'] = dataframe['Order Date'].str[0:2]
    dataframe['Month'] = dataframe['Month'].astype('int32')

    dataframe['Month 2'] = pd.to_datetime(dataframe['Order Date']).dt.month
    dataframe['City'] = dataframe['Purchase Address'].apply(lambda x: f"{GetCity(x)}  ({GetState(x)})")


def GetBestMonth(dataframe):
    dataframe['Sales'] = dataframe['Quantity Ordered'].astype('int') * dataframe['Price Each'].astype('float')
    dataframe.groupby(['Month']).sum()
    months = range(1,13)
    print(months)
    plt.bar(months,dataframe.groupby(['Month']).sum()['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month number')
    plt.show()


def MostSoldCity(dataframe):
    dataframe.groupby(['City']).sum()
    keys = [city for city, df in dataframe.groupby(['City'])]
    plt.bar(keys, dataframe.groupby(['City']).sum()['Sales'])
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month number')
    plt.xticks(keys, rotation='vertical', size=8)
    plt.show()


def AdTime(dataframe):
    # Add hour column
    dataframe['Hour'] = pd.to_datetime(dataframe['Order Date']).dt.hour
    dataframe['Minute'] = pd.to_datetime(dataframe['Order Date']).dt.minute
    dataframe['Count'] = 1
    dataframe.head()
    keys = [pair for pair, df in dataframe.groupby(['Hour'])]
    plt.plot(keys, dataframe.groupby(['Hour']).count()['Count'])
    plt.xticks(keys)
    plt.grid()
    plt.show()

