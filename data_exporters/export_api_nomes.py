import sqlite3
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_data(data, *args, **kwargs):
    """
    Exportar os dados da api de nomes do IBGE para o duckdb
    """
    # Specify your data exporting logic here
    con = sqlite3.connect(database='dw.db')
    con.execute('''
        CREATE TABLE IF NOT EXISTS NOMES(
        nome TEXT,
        frequencia INTEGER,
        ranking INTEGER,
        decada INTEGER,
        sexo TEXT,
        localidade TEXT)
        ''')
    data.to_sql('NOMES', con, if_exists='replace', index=False)
    con.close()