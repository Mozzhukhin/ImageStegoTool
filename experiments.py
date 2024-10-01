import os
from image_utils import load_image, save_image
import numpy as np


def brightness_experiment(image_path):
    """Выполняет эксперимент по изменению яркости изображения и проверяет видимость изменений для каждого цветового канала"""
    image = load_image(image_path)

    # Папка для сохранения изображений
    base_output_folder = "brightness"

    # Цветовые каналы: 0 - Красный, 1 - Зеленый, 2 - Синий
    channels = {
        0: "red",
        1: "green",
        2: "blue"
    }

    # Начало эксперимента для каждого канала
    for channel, color_name in channels.items():
        # Создаем папку для каждого цветового канала
        output_folder = os.path.join(base_output_folder, color_name)
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        print(f"\nНачало эксперимента по изменению яркости для {color_name} канала.")

        for bit in range(8):
            modified_image = image.copy()
            modified_image[:, :, channel] ^= (1 << bit)  # Меняем бит в каждом пикселе для данного цветового канала

            output_name = os.path.join(output_folder, f'brightness_experiment_{color_name}_{bit}.bmp')
            save_image(modified_image, output_name)
            print(f"Изображение с изменениями в {bit}-м бите для {color_name} канала сохранено как {output_name}.")
            print(f"Пожалуйста, сравните исходное изображение с {output_name} для определения видимости изменений.")
