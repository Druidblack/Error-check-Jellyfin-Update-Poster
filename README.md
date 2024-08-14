# Error check Jellyfin Update Poster

Program for Checking the Jellyfin Media Library for Compliance with Requirements for the [Jellyfin Update Poster](https://github.com/Iceshadow1404/JellyfinUpdatePoster) Application

The program will check the media library for missing release years in movies and TV shows. Additionally, if you're using a file system other than NTFS, it will check the filenames of your media files for the permissible number of characters. Upon completion, a file named jellyfin_metadata.txt will be created in the root folder of the program. The file will contain information about problematic titles with comments.

## Setup
Edit config.py.

```
JELLYFIN_SERVER_URL = "http://192.168.1.161:8096"  # URL вашего сервера Jellyfin
API_KEY = "5ca0bf9a4b7a4ce89b3293f21ed8f5f2"  # Ваш API-ключ для аутентификации

```

Программа для проверки медиатеки jellyfin на соблюдение условия необходимых для работы приложения [Jellyfin Update Poster](https://github.com/Iceshadow1404/JellyfinUpdatePoster)
Программа проверит медиатеку на отсутствие года выпуска в фильмах и сериалах, а так же если вы используете файловую систему отличную от NTFS, проверит имена ваших медиафайлов на допустимое количество символов.
По окончанию работы в корне папки программы будет создан файл jellyfin_metadata.txt
В файле буду сохранены данные о проблемных тайтлах с комментариями.

## Настройка
Отредактируйте config.py
```
JELLYFIN_SERVER_URL = "http://192.168.1.161:8096"  # URL вашего сервера Jellyfin
API_KEY = "5ca0bf9a4b7a4ce89b3293f21ed8f5f2"  # Ваш API-ключ для аутентификации

```
