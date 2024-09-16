import pandas as pd
import yaml

def load_data(config):
    df = config['db']
    return pd.read_csv(df,sep=";")

def process_data(df, config):
    df.dropna(subset=['Valor de Venda', 'Valor de Compra'], inplace=True)
    return df

def save_processed_data(df, filename='processed_data.csv'):
    df.to_csv(filename, index=False)
