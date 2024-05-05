def calculate_password(n):
    result = ''
    for i in range(1, n):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

n = int(input("Введите число от 3 до 20: "))
if n < 3 or n > 20:
    print("Число должно быть от 3 до 20")
else:
    password = calculate_password(n)
    print(f"Пароль для числа {n}: {password}")