import sqlite3
import csv
import pandas as pd
from datetime import datetime

conn = sqlite3.connect('database.db')
extraction_datetime = datetime.now()
stocks_file = "./input/stocks.csv"

df: pd.DataFrame = pd.read_csv(stocks_file, usecols=['ticker','cnpj','razao_social','valor_2021'])

#seta as colunas pra caixa baixa
df.columns = [x.lower() for x in df.columns]

df.rename(columns={'valor_2021':'price_2021'}, inplace=True)

df['extraction_date'] = extraction_datetime

cursor = conn.cursor()

def create_database():
    try:
        df.to_sql('stocks', conn, if_exists='replace', index=False, dtype={'ticker':'VARCHAR'})

        print("CRIAÇÃO DA BASE EXECUTADA COM SUCESSO")

        conn.commit()
    except Exception as ex:
        print("ERRO AO CRIAR A BASE DE DADOS, VERIFIQUE AS MENSAGENS DE ERRO {ex}")
    finally:
        print (df)
        print("FINALIZADO COM SUCESSO!")

create_database()