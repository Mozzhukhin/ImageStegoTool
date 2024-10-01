def read_text(path):
    """Читает текст из файла"""
    print(f"Чтение текста из файла {path}")
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    print(f"Прочитано {len(content)} символов.")
    return content

def write_text(path, content):
    """Записывает текст в файл"""
    print(f"Запись текста в файл {path}")
    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)
    print("Текст успешно записан.")
