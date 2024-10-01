import numpy as np
import random


def lsb_hide(image, message):
    """Скрывает текстовое сообщение в изображении методом LSB"""
    # Преобразуем сообщение в двоичный вид
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    flat_image = image.flatten()

    # Проверка на размер сообщения
    if len(binary_message) > len(flat_image):
        raise ValueError("Сообщение слишком велико для данного изображения.")

    # Процесс скрытия сообщения
    for i in range(len(binary_message)):
        pixel_value = int(flat_image[i])  # Преобразуем пиксель в int для безопасности
        # Изменяем младший бит
        flat_image[i] = np.uint8((pixel_value & ~1) | int(binary_message[i]))  # Применяем операцию с учетом uint8

    return flat_image.reshape(image.shape)


def lsb_extract(image):
    """Извлекает текстовое сообщение из изображения методом LSB"""
    flat_image = image.flatten()
    bits = [str(flat_image[i] & 1) for i in range(len(flat_image))]
    binary_message = ''.join(bits)

    chars = [chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)]
    message = ''.join(chars).split('\x00')[0]  # Останавливаемся на первом символе конца строки
    return message


def random_permutation_hide(image, message, key):
    """Скрывает сообщение в изображении методом псевдослучайной перестановки"""
    print("Начало работы метода псевдослучайной перестановки.")

    # Преобразуем сообщение в двоичный формат
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    # Добавляем длину сообщения в начало
    message_length = len(binary_message)
    binary_message = format(message_length, '032b') + binary_message

    print(f"Сообщение преобразовано в двоичный формат. Длина сообщения: {len(binary_message)} бит.")

    flat_image = image.flatten()

    if len(binary_message) > len(flat_image):
        raise ValueError("Сообщение слишком велико для данного изображения.")

    # Генерация псевдослучайной перестановки на основе ключа
    random.seed(key)
    indices = list(range(len(flat_image)))
    random.shuffle(indices)

    print("Начало скрытия сообщения...")
    for i in range(len(binary_message)):
        pixel_value = int(flat_image[indices[i]])  # Преобразование в int
        flat_image[indices[i]] = np.uint8((pixel_value & ~1) | int(binary_message[i]))  # Преобразование в uint8

    print("Сообщение скрыто с использованием псевдослучайной перестановки.")
    return flat_image.reshape(image.shape)


def random_permutation_extract(image, key):
    """Извлекает сообщение из изображения методом псевдослучайной перестановки"""
    print("Начало извлечения сообщения методом псевдослучайной перестановки.")

    flat_image = image.flatten()

    # Генерация псевдослучайной перестановки на основе ключа
    random.seed(key)
    indices = list(range(len(flat_image)))
    random.shuffle(indices)

    # Сначала извлекаем длину сообщения (32 бита)
    length_bits = [str(flat_image[indices[i]] & 1) for i in range(32)]
    message_length = int(''.join(length_bits), 2)
    print(f"Извлеченная длина сообщения: {message_length} бит.")

    # Теперь извлекаем само сообщение
    bits = [str(flat_image[indices[i + 32]] & 1) for i in range(message_length)]
    binary_message = ''.join(bits)

    print("Сообщение в двоичном формате извлечено.")
    chars = [chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)]
    message = ''.join(chars).split('\x00')[0]
    return message


def random_interval_hide(image, message, key):
    """Скрывает сообщение в изображении методом псевдовыпадкового интервала"""
    print("Начало работы метода псевдовыпадкового интервала.")

    # Преобразуем сообщение в двоичный формат
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    message_length = len(binary_message)
    binary_message = format(message_length, '032b') + binary_message  # Добавляем длину сообщения

    flat_image = image.flatten()

    if len(binary_message) > len(flat_image):
        raise ValueError("Сообщение слишком велико для данного изображения.")

    # Генерация псевдовыпадковых интервалов на основе ключа
    random.seed(key)
    interval = random.randint(1, 10)  # Начальный интервал (заданный случайно от 1 до 10)
    current_index = 0

    print("Начало скрытия сообщения...")
    for bit in binary_message:
        # Скрываем бит в младшем бите пикселя
        pixel_value = int(flat_image[current_index])
        flat_image[current_index] = np.uint8((pixel_value & ~1) | int(bit))

        # Генерируем новый интервал на основе ключа
        interval = random.randint(1, 10)
        current_index += interval

        if current_index >= len(flat_image):
            raise ValueError("Интервалы слишком велики для данного изображения.")

    print("Сообщение скрыто с использованием метода псевдовыпадкового интервала.")
    return flat_image.reshape(image.shape)


def random_interval_extract(image, key):
    """Извлекает сообщение из изображения методом псевдовыпадкового интервала"""
    print("Начало извлечения сообщения методом псевдовыпадкового интервала.")

    flat_image = image.flatten()

    # Генерация псевдовыпадковых интервалов на основе ключа
    random.seed(key)
    interval = random.randint(1, 10)  # Начальный интервал
    current_index = 0

    # Сначала извлекаем длину сообщения (32 бита)
    length_bits = []
    for _ in range(32):
        length_bits.append(str(flat_image[current_index] & 1))
        interval = random.randint(1, 10)
        current_index += interval

    message_length = int(''.join(length_bits), 2)
    print(f"Извлеченная длина сообщения: {message_length} бит.")

    # Теперь извлекаем само сообщение
    bits = []
    for _ in range(message_length):
        bits.append(str(flat_image[current_index] & 1))
        interval = random.randint(1, 10)
        current_index += interval

    binary_message = ''.join(bits)

    print("Сообщение в двоичном формате извлечено.")
    chars = [chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8)]
    message = ''.join(chars).split('\x00')[0]
    return message
