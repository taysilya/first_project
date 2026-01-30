# main.py

def print_author():
    """
    Читает значение переменной AUTHOR из файла .env и выводит имя автора
    """
    author = None  # Инициализируем переменную
    
    try:
        # Открываем файл .env для чтения
        with open(".env", "r", encoding="utf-8") as file:
            # Читаем файл построчно
            for line in file:
                line = line.strip()  # Убираем пробелы в начале и конце
                
                # Пропускаем пустые строки и комментарии
                if not line or line.startswith("#"):
                    continue
                
                # Проверяем, начинается ли строка с AUTHOR=
                if line.startswith("AUTHOR="):
                    # Разделяем строку по первому знаку '='
                    parts = line.split("=", 1)
                    if len(parts) == 2:
                        # Берем значение после '=', убираем пробелы и кавычки
                        author = parts[1].strip()
                        
                        # Убираем кавычки если они есть
                        if (author.startswith('"') and author.endswith('"')) or \
                           (author.startswith("'") and author.endswith("'")):
                            author = author[1:-1]
                        break  # Переменная найдена, выходим из цикла
        
        # Если переменная не найдена
        if author is None:
            author = "Неизвестный автор"
            
    except FileNotFoundError:
        # Если файл .env не существует
        author = "Файл .env не найден"
    except Exception as e:
        # Другие возможные ошибки
        author = f"Ошибка чтения: {e}"
    
    # Выводим результат
    print(f"Автор проекта: {author}")


# Вызываем функцию при запуске файла
if __name__ == "__main__":
    print_author()
