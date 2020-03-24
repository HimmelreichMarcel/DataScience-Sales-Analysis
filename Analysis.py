import pandas as pd
import matplotlib.pyplot as plt
import os


def merge_data(files, path):
    all_data = pd.DataFrame()
    for file in files:
        current_data = pd.read_csv(path + "/" + file)
        all_data = pd.concat([all_data, current_data])
    return all_data


def clean_data(dataframe):
    # Find NAN
    nan_df = dataframe[dataframe.isna().any(axis=1)]

    dataframe = dataframe.dropna(how='all')

    dataframe = dataframe[dataframe['Order Date'].str[0:2] != 'Or']

    dataframe['Quantity Ordered'] = pd.to_numeric(dataframe['Quantity Ordered'])
    dataframe['Price Each'] = pd.to_numeric(dataframe['Price Each'])
    return dataframe


def get_city(address):
    return address.split(",")[1].strip(" ")


def get_state(address):
    return address.split(",")[2].split(" ")[1]


def preprocess_data(dataframe):
    dataframe['Month'] = dataframe['Order Date'].str[0:2]
    dataframe['Month'] = dataframe['Month'].astype('int32')

    dataframe['Month 2'] = pd.to_datetime(dataframe['Order Date']).dt.month
    dataframe['City'] = dataframe['Purchase Address'].apply(lambda x: f"{GetCity(x)}  ({GetState(x)})")
    return dataframe


def get_best_month(dataframe, path):
    dataframe['Sales'] = dataframe['Quantity Ordered'].astype('int') * dataframe['Price Each'].astype('float')
    dataframe.groupby(['Month']).sum()
    months = range(1,13)
    print(months)
    plt.bar(months,dataframe.groupby(['Month']).sum()['Sales'])
    plt.xticks(months)
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month number')
    plt.savefig(path, dpi=100)
    plt.show()


def most_sold_city(dataframe, path):
    dataframe.groupby(['City']).sum()
    keys = [city for city, df in dataframe.groupby(['City'])]
    plt.bar(keys, dataframe.groupby(['City']).sum()['Sales'])
    plt.ylabel('Sales in USD ($)')
    plt.xlabel('Month number')
    plt.xticks(keys, rotation='vertical', size=8)
    plt.savefig(path, dpi=100)
    plt.show()


def ad_time(dataframe, path):
    # Add hour column
    dataframe['Hour'] = pd.to_datetime(dataframe['Order Date']).dt.hour
    dataframe['Minute'] = pd.to_datetime(dataframe['Order Date']).dt.minute
    dataframe['Count'] = 1
    dataframe.head()
    keys = [pair for pair, df in dataframe.groupby(['Hour'])]
    plt.plot(keys, dataframe.groupby(['Hour']).count()['Count'])
    plt.xticks(keys)
    plt.xlabel("Daytime in Hours")
    plt.ylabel("Sales Count")
    plt.savefig(path, dpi=100)
    plt.grid()
    plt.show()