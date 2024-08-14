# utils.py

from typing import List

def save_to_file(data: List[str], filename: str = "jellyfin_metadata.txt") -> None:
    """
    Сохраняет данные в текстовый файл.
    
    :param data: Список строк для записи.
    :param filename: Имя файла, в который будут записаны данные.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("\n\n".join(data))
