import os

print(os.path.abspath(os.path.dirname("2.2_4.py")))

print(os.path.abspath("2.2_4.py"))

print("\n===============================================\n")
# --- Способ 1: через os.path ---
# Получаем папку, где лежит исполняемый файл

# Путь к папке с тестами
current_dir = os.path.dirname("2.2_7.py") # current_dir = C:\Users\niseg\Desktop\AT\first\main\2.2

# Путь к файлу в папке data (на уровень выше)
file_path = os.path.join(current_dir, "..", "2.1", "2.1_5.py")

# Преобразуем в абсолютный путь
file_path = os.path.abspath(file_path)

# Проверим, что файл существует
assert os.path.exists(file_path), f"Файл не найден: {file_path}"


# --- Способ 2: через pathlib (современный способ) ---
# Получаем путь к текущему файлу и поднимаемся на уровень выше к корню

from pathlib import Path

project_root = Path(__file__).parent.parent  # parent.parent = main/
file_path_pathlib = project_root / "2.1" / "2.1_5.py"

# Преобразуем в абсолютный путь
file_path_pathlib = file_path_pathlib.resolve()

print("Путь через pathlib:", file_path_pathlib)


print(Path(__file__))
