import matplotlib.pyplot as plt
import seaborn as sns

def gerar_graficos(df, config):
    var_comparacao = config['var_comparacao']
    var_agrupamento = config['var_agrupamento']

    for var in var_comparacao:
        plt.figure(figsize=(9, 6))
        sns.boxplot(x=var, y=var_comparacao[0], data=df)
        plt.title(f'Comparação de {var_comparacao[0]} por {var}')
        plt.savefig(f"{config['output_dir']}{var_comparacao[0]}_por_{var}.png")

        plt.figure(figsize=(9, 6))
        sns.boxplot(x=var, y=var_comparacao[1], data=df)
        plt.title(f'Comparação de {var_comparacao[1]} por {var}')
        plt.savefig(f"{config['output_dir']}{var_comparacao[1]}_por_{var}.png")
