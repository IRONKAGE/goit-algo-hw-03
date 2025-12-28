import argparse
import shutil
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання та сортування файлів за розширенням.")
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    parser.add_argument(
        "dest", 
        type=Path, 
        nargs="?", 
        default=Path("dist"), 
        help="Шлях до директорії призначення (за замовчуванням 'dist')"
    )
    return parser.parse_args()

def recursive_copy(source_dir: Path, dest_dir: Path):
    try:
        if not source_dir.exists():
            print(f"Помилка: Вихідна директорія '{source_dir}' не існує.")
            return

        for item in source_dir.iterdir():
            try:
                if item.is_dir():
                    recursive_copy(item, dest_dir)
                elif item.is_file():
                    copy_file_to_extension_subdir(item, dest_dir)
            except PermissionError:
                print(f"Помилка доступу до об'єкта: {item}")
            except Exception as e:
                print(f"Непередбачена помилка при обробці {item}: {e}")

    except PermissionError:
        print(f"Відмовлено в доступі до директорії: {source_dir}")
    except Exception as e:
        print(f"Сталася помилка при читанні {source_dir}: {e}")

def copy_file_to_extension_subdir(file_path: Path, dest_root: Path):
    ext = file_path.suffix.lower().replace(".", "")
    
    if not ext:
        ext = "no_extension"
    
    target_dir = dest_root / ext
    
    try:
        target_dir.mkdir(parents=True, exist_ok=True)
        
        shutil.copy2(file_path, target_dir / file_path.name)
    except Exception as e:
        print(f"Не вдалося скопіювати файл {file_path}: {e}")

def main():
    args = parse_arguments()
    
    source = args.source
    destination = args.dest

    print(f"Початок роботи...")
    print(f"Джерело: {source.absolute()}")
    print(f"Призначення: {destination.absolute()}")

    try:
        destination.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        print(f"Критична помилка: Не вдалося створити директорію призначення: {e}")
        return

    recursive_copy(source, destination)
    print("Обробку завершено.")

if __name__ == "__main__":
    main()
    
# Запустити даний скрипт можна з терміналу, ввівши: python3 ./task_1.py ./
