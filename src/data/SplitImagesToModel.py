import os
import shutil
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


def split_images(input_dirs, output_dir, seed=None, train_size=0.7, val_size=0.15, test_size=0.15):
    # Verificar se as proporções somam 1
    if train_size + val_size + test_size != 1:
        raise ValueError("As proporções de treino, validação e teste devem somar 1.")

    if seed is not None:
        random.seed(seed)

    # Iterar por cada diretório de classe na lista de input_dirs
    for class_dir in input_dirs:
        class_name = os.path.basename(class_dir)  # Nome da classe baseado na pasta
        print(f"A processar a classe: {class_name}")

        # Criar pastas de destino para cada classe (train, validation, test)
        for folder in ['train', 'validation', 'test']:
            os.makedirs(os.path.join(output_dir, folder, class_name), exist_ok=True)

        # Obter a lista de todas as imagens no diretório de input
        images = [f for f in os.listdir(class_dir) if os.path.isfile(os.path.join(class_dir, f))]

        # Baralhar as imagens
        random.shuffle(images)

        # Determinar quantas imagens em cada divisão
        total_images = len(images)
        train_count = int(total_images * train_size)
        val_count = int(total_images * val_size)

        # Dividir as imagens em treino, validação e teste
        train_images = images[:train_count]
        val_images = images[train_count:train_count + val_count]
        test_images = images[train_count + val_count:]

        # Função para copiar as imagens para os diretórios corretos
        def copy_images(image_list, destination_folder):
            for image in image_list:
                src = os.path.join(class_dir, image)
                dst = os.path.join(output_dir, destination_folder, class_name, image)
                shutil.copy(src, dst)

        # Copiar as imagens para treino, validação e teste
        copy_images(train_images, 'train')
        copy_images(val_images, 'validation')
        copy_images(test_images, 'test')

        print(f"Classe '{class_name}' - {train_count} treino, {val_count} validação, {len(test_images)} teste.\n")

    print("Distribuição concluída.")