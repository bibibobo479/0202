def generate_random_list(n):
    """
    Генерирует список случайных чисел (объединенная версия)
    """
    min_value = 5  # из main
    max_value = n * 200  # из feature-branch (более широкий диапазон)
    num_elements = n + 15  # из main
    
    # Используем list comprehension из feature-branch
    random_list = [random.randint(min_value, max_value) for _ in range(num_elements)]
    
    # Добавляем умножение из main для увеличения значений
    random_list = [x * 2 for x in random_list]
    
    return random_list
