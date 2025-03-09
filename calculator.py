# Простой калькулятор
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a + b

def percentage(total, percent):
    return (total * percent) / 100

# Тестим функции
print("Сложение: ", add(5, 3))      # Вывод: 8
print("Вычитание: ", subtract(10, 4)) # Вывод: 6
print("Умножение: ", multiply(2, 3))  # Вывод: 6
print("Деление: ", divide(8, 2))     # Вывод: 4.0
print("Степень: ", power(2, 3))      # Вывод: 8
print("Процент: ", percentage(200, 50)) # Вывод: 100.0
print("Процент 2: ", percentage(50, 10)) # Вывод: 5.0