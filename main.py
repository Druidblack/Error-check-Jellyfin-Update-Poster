# main.py

from api_client import fetch_metadata
from data_processor import process_metadata
from utils import save_to_file

def main():
    # Получаем метаданные фильмов и сериалов
    items = fetch_metadata()
    
    # Обрабатываем полученные данные
    processed_data = process_metadata(items)
    
    # Сохраняем данные в файл
    save_to_file(processed_data)
    
    print(f"Данные успешно сохранены в файл.")

if __name__ == "__main__":
    main()
