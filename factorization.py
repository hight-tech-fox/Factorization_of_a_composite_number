import tkinter as tk
from tkinter import filedialog
import random
import time


"Генерация случайного числа"


def generate_random_number(n):
    n = n - 1
    return random.randint(1, n)


"Нахождение НОД двух чисел"


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


"Функция F (из алгоритма)"


def f(x):
    return x**2 + 1


"Проверка на простоту тестом Рабина-Миллера (6 лр)"


def check_miller_rabin(n, k=40):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2
    for _ in range(k):
        a = random.randrange(1, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2 * s, n)
            if x == n - 1:
                break
        else:
            return False
    return True


"Полная факторизация"


def factorization(n):
    prime_factors = []

    def factorize_last_number(num, factors_list):
        if num < 2:
            return
        for i in range(2, int(num ** 0.5) + 1):
            while num % i == 0:
                factors_list.append(i)
                num //= i
        if num > 1:
            factors_list.append(num)

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    x = generate_random_number(n)
    y = x
    x_i = x
    k = 2
    for i in range(2, n + 1):
        x = x_i
        x_i = f(x) % n
        d = gcd(abs(y - x_i), n)
        if 1 < d < n:
            if check_miller_rabin(d):
                prime_factors.append(d)
                n //= d
                continue
        else:
            if i < k:
                continue
            if i == k:
                y = x_i
                k *= 2
                continue

    if n > 1:
        m = n

    if prime_factors:
        factorize_last_number(m, prime_factors)

    return prime_factors


"Главная функция обработки n"


def main(n):
    start_time = time.time()
    file_path_output = "output_data.txt"

    try:
        if n < 1:
            result = "Неверные входные данные"
        elif n == 1:
            result = "Число n = 1 не является простым или составным"
        elif check_miller_rabin(n):
            result = "n - простое число"
        else:
            result = "n - составное,\nразложение на простые множители:\n"
            result += str(factorization(n))

        with open(file_path_output, "w") as output_file:
            output_file.write(result)
            end_time = time.time()
            execution_time = end_time - start_time
            print(f"Результат сохранен в файл '{file_path_output}' 📝")
            print(f"Время выполнения: {execution_time:.5f} сек.")

            # Добавление времени выполнения в окно tkinter
            result += f"\n\nВремя выполнения: {execution_time:.5f} сек."
            label_result.config(text=result)

    except Exception as e:
        print(f"Произошла ошибка: {e} 💥")


"Чтение с файла и обработка неврного типа данных"


def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Выберите файл с входными данными")
    if file_path:
        try:
            with open(file_path, "r") as file:
                try:
                    n = int(file.readline().strip())
                    main(n)
                except ValueError:
                    label_result.config(text="Неверный формат входных данных")
        except FileNotFoundError:
            print(f"Файл '{file_path}' не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e} 💥")


"Базовый интерфейс на tkinter"


root = tk.Tk()
root.title("Факторизация числа n")
root.geometry("300x130")

button_open = tk.Button(root, text="Открыть файл", command=open_file_dialog)
button_open.pack()

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()