import os
import matplotlib.pyplot as plt
import seaborn as sns

def contar_imagens_em_pastas(pastas):
    extensoes_imagem = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')
    contagem = {}

    for pasta in pastas:
        if os.path.exists(pasta) and os.path.isdir(pasta):
            num_imagens = 0
            for root, dirs, files in os.walk(pasta):
                num_imagens += sum(1 for file in files if file.lower().endswith(extensoes_imagem))
            # Usar apenas o nome da última pasta
            nome_pasta = os.path.basename(os.path.normpath(pasta))
            contagem[nome_pasta] = num_imagens
        else:
            nome_pasta = os.path.basename(os.path.normpath(pasta))
            contagem[nome_pasta] = 0  # Pasta não encontrada ou não é uma diretoria
    return contagem

def criar_barplot(contagem):
    pastas = list(contagem.keys())
    num_imagens = list(contagem.values())

    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=num_imagens, y=pastas, palette="viridis", hue=pastas, dodge=False, legend=False, orient='h')

    plt.ylabel('Oral Diseases')
    plt.xlabel('Número de Imagens')
    plt.title('Number of images of each oral disease')
    # plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
