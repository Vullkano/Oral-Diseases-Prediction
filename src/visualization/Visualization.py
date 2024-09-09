import os
import matplotlib.pyplot as plt
import seaborn as sns
import random
from PIL import Image
from pathlib import Path
import shutil

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


def get_random_images_from_dir(directory, num_images):
    all_images = [os.path.join(directory, img) for img in os.listdir(directory) if img.endswith(('.jpg', '.jpeg', '.png'))]
    if len(all_images) < num_images:
        return all_images
    return random.sample(all_images, num_images)


def show_random_images(OralDiseaseClasses:list, num_images_per_class=2, num_images_per_row=4, seed=42):
    # Set seed for reproducibility
    random.seed(seed)

    # Create a figure
    num_rows = (
                           len(OralDiseaseClasses) * num_images_per_class + num_images_per_row - 1) // num_images_per_row  # Calculate number of rows needed
    fig, axs = plt.subplots(num_rows, num_images_per_row, figsize=(15, num_rows * 2.5))
    fig.suptitle('Random Images from Each Class', fontsize=16)

    # Flatten axs array for easier indexing
    axs = axs.flatten()

    # Iterate through classes and display images
    image_idx = 0

    base_dir = Path(os.getcwd()).resolve().parent
    data_dir = base_dir / 'data'
    for class_name in OralDiseaseClasses:
        class_dir = os.path.join(data_dir, 'train', class_name)
        random_images = get_random_images_from_dir(class_dir, num_images_per_class)

        for img_path in random_images:
            if image_idx < len(axs):
                img = Image.open(img_path)
                ax = axs[image_idx]
                ax.imshow(img)
                ax.set_title(class_name)
                ax.axis('off')
                image_idx += 1

    # Hide any unused subplots
    for i in range(image_idx, len(axs)):
        axs[i].axis('off')

    # Adjust layout and show the plot
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()
