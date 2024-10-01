from PIL import Image
import numpy as np

def load_image(path):
    """Загружает изображение в формате BMP и преобразует его в массив"""
    print(f"Попытка загрузки изображения из {path}")
    image = Image.open(path)
    image_array = np.array(image)
    print(f"Изображение загружено. Размер изображения (высота, ширина, каналы): {image_array.shape}")
    return image_array

def save_image(image_array, path):
    """Сохраняет изображение из массива в формате BMP"""
    print(f"Сохранение изображения по адресу {path}")
    image = Image.fromarray(image_array)
    image.save(path)
    print("Изображение успешно сохранено.")
