import os

def delete_file(path):
    # Проверяем существование файла
    if not os.path.exists(path):
        print(f"Файл {path} не существует.")
        return

    # Проверяем доступ к файлу для записи
    if not os.access(path, os.W_OK):
        print(f"Нет доступа к записи в файл {path}.")
        return

    # Удаляем файл
    try:
        os.remove(path)
        print(f"Файл {path} успешно удален.")
    except Exception as e:
        print(f"Произошла ошибка при удалении файла {path}: {e}")

# Указываем путь к файлу, который нужно удалить
specified_path = "/path/to/your/file"

# Удаляем файл по указанному пути
delete_file(specified_path)
