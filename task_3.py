def solve_hanoi(n, source, auxiliary, destination, disk_storage):
    if n == 1:
        disk = disk_storage[source].pop()
        disk_storage[destination].append(disk)
        print(f"Перемістити диск {disk} з {source} на {destination}")
        print(f"Проміжний стан: {disk_storage}")
        return

    solve_hanoi(n - 1, source, destination, auxiliary, disk_storage)

    disk = disk_storage[source].pop()
    disk_storage[destination].append(disk)
    print(f"Перемістити диск {disk} з {source} на {destination}")
    print(f"Проміжний стан: {disk_storage}")

    solve_hanoi(n - 1, auxiliary, source, destination, disk_storage)

def run_hanoi_game():
    try:
        n_disks_str = input("Введіть кількість дисків (n): ")
        n_disks = int(n_disks_str)
        
        if n_disks <= 0:
            print("Кількість дисків має бути додатним цілим числом.")
            return

        initial_disks = list(range(n_disks, 0, -1))
        
        pegs = {
            'A': initial_disks,
            'B': [],
            'C': []
        }
        
        print(f"\nПочатковий стан: {pegs}")
        
        solve_hanoi(n_disks, 'A', 'B', 'C', pegs)
        
        print(f"Кінцевий стан: {pegs}")
        print(f"Загальна мінімальна кількість кроків: {2**n_disks - 1}")

    except ValueError:
        print("Помилка вводу. Будь ласка, введіть коректне ціле число.")
    except Exception as e:
        print(f"Виникла помилка: {e}")

if __name__ == "__main__":
    run_hanoi_game()
