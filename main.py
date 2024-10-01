from image_utils import load_image, save_image
from steganography import lsb_hide, lsb_extract, random_permutation_hide, random_permutation_extract, random_interval_hide, random_interval_extract
from experiments import brightness_experiment
from utils import read_text, write_text

# Статические переменные
IMAGE_PATH = "images/homiak.bmp"
MESSAGE_PATH = "message.txt"
OUTPUT_IMAGE = "output.bmp"
KEY = "my_secret_key"  # Пример ключа для псевдослучайной перестановки или метода псевдослучайного интервала


def main_menu():
    while True:
        print("\nВыберите задачу:")
        print("1. Скрыть сообщение методом LSB")
        print("2. Извлечь сообщение методом LSB")
        print("3. Эксперимент по порогу чувствительности")
        print("4. Скрыть сообщение методом псевдослучайной перестановки")
        print("5. Извлечь сообщение методом псевдослучайной перестановки")
        print("6. Скрыть сообщение методом псевдослучайного интервала")
        print("7. Извлечь сообщение методом псевдослучайного интервала")
        print("0. Выйти из программы")

        choice = input("Введите номер задачи: ")

        if choice == "1":
            # Скрытие сообщения методом LSB
            print("\nВы выбрали: Скрыть сообщение методом LSB.")
            image = load_image(IMAGE_PATH)
            print(f"Размер изображения: {image.shape}")
            message = read_text(MESSAGE_PATH)
            print("Начало процесса скрытия сообщения...")
            stego_image = lsb_hide(image, message)
            save_image(stego_image, OUTPUT_IMAGE)
            print(f"Стеганограмма сохранена как {OUTPUT_IMAGE}.\n")

        elif choice == "2":
            # Извлечение сообщения методом LSB
            print("\nВы выбрали: Извлечь сообщение методом LSB.")
            image = load_image(OUTPUT_IMAGE)
            message = lsb_extract(image)
            print(f"\nИзвлеченное сообщение: {message}\n")

        elif choice == "3":
            # Эксперимент по порогу чувствительности
            print("\nВы выбрали: Эксперимент по порогу чувствительности.")
            print("\nЗагрузка изображения...")
            brightness_experiment(IMAGE_PATH)

        elif choice == "4":
            # Скрытие сообщения методом псевдослучайной перестановки
            print("\nВы выбрали: Скрыть сообщение методом псевдослучайной перестановки.")
            image = load_image(IMAGE_PATH)
            message = read_text(MESSAGE_PATH)
            stego_image = random_permutation_hide(image, message, KEY)
            save_image(stego_image, OUTPUT_IMAGE)
            print(f"Стеганограмма сохранена как {OUTPUT_IMAGE}.\n")

        elif choice == "5":
            # Извлечение сообщения методом псевдослучайной перестановки
            print("\nВы выбрали: Извлечь сообщение методом псевдослучайной перестановки.")
            image = load_image(OUTPUT_IMAGE)
            message = random_permutation_extract(image, KEY)
            print(f"\nИзвлеченное сообщение: {message}\n")

        elif choice == "6":
            # Скрытие сообщения методом псевдослучайного интервала
            print("\nВы выбрали: Скрыть сообщение методом псевдослучайного интервала.")
            image = load_image(IMAGE_PATH)
            message = read_text(MESSAGE_PATH)
            stego_image = random_interval_hide(image, message, KEY)
            save_image(stego_image, OUTPUT_IMAGE)
            print(f"Стеганограмма сохранена как {OUTPUT_IMAGE}.\n")

        elif choice == "7":
            # Извлечение сообщения методом псевдослучайного интервала
            print("\nВы выбрали: Извлечь сообщение методом псевдослучайного интервала.")
            image = load_image(OUTPUT_IMAGE)
            message = random_interval_extract(image, KEY)
            print(f"\nИзвлеченное сообщение: {message}\n")

        elif choice == "0":
            print("\nВыход из программы.")
            break

        else:
            print("Неверный ввод, пожалуйста, выберите корректный пункт.")


if __name__ == "__main__":
    main_menu()
