import yaml
from tratamento import load_data, process_data, save_processed_data
from graficos import gerar_graficos
import os

def validar_config(config):
    # Exemplo de validação simples
    required_keys = ['db', 'var_agrupamento',
                     'var_comparacao', 'output_dir']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Configuração faltando: {key}")

    # Verifica se o diretório de saída existe
    if not os.path.exists(config['output_dir']):
        os.makedirs(config['output_dir'])

def main():
    # Carrega o YAML
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)

    # Valida a configuração
    validar_config(config)

    # Carrega e processa os dados
    df = load_data(config)
    df = process_data(df, config)

    # Salva os dados processados (opcional)
    save_processed_data(df)

    # Gera gráficos
    gerar_graficos(df, config)

if __name__ == '__main__':
    main()
