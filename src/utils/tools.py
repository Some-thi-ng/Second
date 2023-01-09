from django.core.exceptions import ValidationError
import os

def get_path_upload_avatar(instance, file):
    # Построение пути к файлу аватара
    return f'user_{instance.id}/avatar/{file}'

def get_path_upload_image(instance, file):
    # Построение пути к файлу image
    return f'user_{instance.user.id}/gallery/{file}'

def validate_size_image(file_obj):
    # Валидация размера загружаемого изображения
    size_limit = 5
    if file_obj.size > size_limit * 1024 * 1024:
        return ValidationError(f'Максимальный размер загружаемого файла {size_limit}Mb')

def delete_old_file(path_file):
    # Удаление старого файла
    if os.path.exists(path_file):
        os.remove(path_file)
