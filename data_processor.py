# data_processor.py

import os
from typing import List, Dict, Any
from config import JELLYFIN_SERVER_URL

MAX_NAME_LENGTH = 136  # Максимально допустимая длина имени

def has_no_release_year(year: Any) -> bool:
    """
    Проверяет, отсутствует ли информация о годе выпуска.
    
    :param year: Год выпуска, может быть None или другим некорректным значением.
    :return: True, если информация о годе выпуска отсутствует, иначе False.
    """
    return year is None or year == 0

def is_title_too_long(name: str) -> bool:
    """
    Проверяет, превышает ли длина названия допустимый предел.
    
    :param name: Название.
    :return: True, если длина названия больше допустимого предела, иначе False.
    """
    return len(name) > MAX_NAME_LENGTH

def shorten_name(name: str, max_length: int) -> str:
    """
    Укорачивает имя до последнего допустимого пробела, чтобы длина не превышала max_length.
    
    :param name: Название.
    :param max_length: Максимально допустимая длина названия.
    :return: Укороченное название.
    """
    if len(name) <= max_length:
        return name
    
    # Обрезаем строку до максимальной длины
    shortened_name = name[:max_length]
    
    # Находим последний пробел в укороченном названии
    last_space_index = shortened_name.rfind(' ')
    
    if last_space_index == -1:
        return shortened_name  # Если пробелов нет, возвращаем как есть
    
    return shortened_name[:last_space_index]

def get_filesystem_type(path: str) -> str:
    """
    Определяет тип файловой системы для заданного пути.
    
    :param path: Путь к директории.
    :return: Тип файловой системы.
    """
    fs_type = os.popen(f"df -T {path} | tail -1 | awk '{{print $2}}'").read().strip()
    return fs_type.upper()

def process_metadata(items: List[Dict[str, Any]]) -> List[str]:
    """
    Обрабатывает список метаданных и формирует строки для записи в файл.
    Фильтрует только те записи, где отсутствует информация о годе выпуска
    или длина названия превышает допустимый предел (только если файловая система не NTFS).
    
    :param items: Список словарей с метаданными фильмов и сериалов.
    :return: Список строк, готовых для записи в текстовый файл.
    """
    processed_items = []
    fs_type = get_filesystem_type(".")
    
    for item in items:
        name = item.get("Name", "Unknown Title")
        year = item.get("ProductionYear", None)
        item_id = item.get("Id")  # Получаем ID элемента
        url = f"{JELLYFIN_SERVER_URL}/web/index.html#!/details?id={item_id}"  # Формируем URL
        
        explanations = []
        if has_no_release_year(year):
            explanations.append("Year missing")
        
        if is_title_too_long(name):
            if fs_type != "NTFS":
                explanations.append("Title length exceeded the allowable limit")
                shortened_name = shorten_name(name, MAX_NAME_LENGTH)
                explanations.append(f"Shortened title: {shortened_name}")
            else:
                continue  # Пропускаем элементы с длинным именем на файловой системе NTFS
        
        if explanations:
            explanation_text = "\n".join(explanations)
            processed_items.append(
                f"Title: {name}\nYear: {year if year else 'Unknown Year'}\nURL: {url}\nExplanation:\n{explanation_text}\n"
            )
    
    return processed_items
