# api_client.py

import requests
from typing import Dict, Any, List
from config import JELLYFIN_SERVER_URL, API_KEY

def get_headers() -> Dict[str, str]:
    """
    Возвращает заголовки для авторизации в API Jellyfin.
    """
    return {
        "X-Emby-Token": API_KEY,
        "Accept": "application/json"
    }

def fetch_metadata() -> List[Dict[str, Any]]:
    """
    Получает все доступные метаданные фильмов и сериалов с сервера Jellyfin.
    
    :return: Список словарей с метаданными фильмов и сериалов.
    """
    url = f"{JELLYFIN_SERVER_URL}/Items"
    params = {
        "IncludeItemTypes": "Movie,Series",  # Получение только фильмов и сериалов
        "Fields": "Name,ProductionYear,Genres,Overview",  # Поля, которые нас интересуют
        "Recursive": "true"
    }
    response = requests.get(url, headers=get_headers(), params=params)
    
    if response.status_code == 200:
        return response.json().get('Items', [])
    else:
        response.raise_for_status()
