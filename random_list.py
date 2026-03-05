def generate_random_list(n):
    """
    Генерирует список случайных чисел (версия из feature-branch)
    """
    min_value = 10  # Изменено с 5 на 10
    max_value = n * 200  # Изменено с *100 на *200
    num_elements = n + 20  # Изменено с +10 на +20
    
    random_list = [random.randint(min_value, max_value) for _ in range(num_elements)]
    return random_list
