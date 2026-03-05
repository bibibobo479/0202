#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random

def generate_random_list(n):
    """
    Генерирует список случайных чисел (версия из main)
    """
    min_value = 5
    max_value = n * 150  # Изменено с *100 на *150
    num_elements = n + 15  # Изменено с +10 на +15
    
    # Используем другой метод генерации
    random_list = []
    for i in range(num_elements):
        random_number = random.randint(min_value, max_value)
        random_list.append(random_number * 2)  # Добавлено умножение
    return random_list

def main():
    # Номер по журналу
    n = 24  # Замените на свой номер
    
    # Генерация списка
    result = generate_random_list(n)
    
    # Вывод результатов
    print(f"Номер по журналу: {n}")
    print(f"Диапазон: от 5 до {n * 100}")
    print(f"Количество элементов: {n + 10}")
    print("Сгенерированный список:")
    print(result)
    
    # Дополнительно: сортировка для наглядности
    print("\nОтсортированный список:")
    print(sorted(result))

if __name__ == "__main__":
    main()
