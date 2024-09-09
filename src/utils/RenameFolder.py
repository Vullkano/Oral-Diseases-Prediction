import os

def rename_folders(directory, old_prefix, new_prefix):
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)

        # Verificar se é uma pasta e se começa com o prefixo antigo
        if os.path.isdir(folder_path) and folder_name.startswith(old_prefix):
            new_name = folder_name.replace(old_prefix, new_prefix, 1)
            new_path = os.path.join(directory, new_name)

            # Renomear a pasta
            os.rename(folder_path, new_path)
            print(f"Renomeada a pasta '{folder_name}' para '{new_name}'.\n")
