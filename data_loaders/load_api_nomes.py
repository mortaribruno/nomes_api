import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Carregar os dados da api de nomes do IBGE por decadas, sexo e localidade
    """
    decadas = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    sexo = ['M','F']
    localidade = [11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,29,31,32,33,35,41,42,43,50,51,52,53]
    dados = pd.DataFrame(columns=['nome','frequencia','ranking','decada','sexo','localidade'])
    for d in decadas:
        for s in sexo:
            for l in localidade:
                url = f"http://servicodados.ibge.gov.br/api/v2/censos/nomes/ranking/?decada={d}&sexo={s}&localidade={l}"
                max_retries = 3
                retries = 0
                success = False
                while not success and retries < max_retries:
                    try:
                        resp_response = requests.get(url)
                        resp_response.raise_for_status()

                        if resp_response.status_code == 200:
                            df_lista = resp_response.json()[0]['res']
                            df = pd.DataFrame(df_lista)
                            df['decada'] = d
                            df['sexo'] = s
                            df['localidade'] = l
                            dados = pd.concat([dados, df], ignore_index=True)
                            success = True
                        else:
                            print(f"HTTP request failed with status code {resp_response.status_code} for URL: {url}")
                    
                    except requests.exceptions.RequestException as e:
                        print(f"HTTP request failed for URL: {url}. Error: {str(e)}")
                
                retries += 1

    return dados


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'