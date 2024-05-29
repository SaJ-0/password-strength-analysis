from zxcvbn import zxcvbn

# Список паролей для анализа
passwords = [
    "123456",
    "password",
    "qwerty",
    "P@ssw0rd!",
    "correcthorsebatterystaple"
]

# Функция для анализа паролей
def analyze_passwords(passwords):
    results = []
    for password in passwords:
        result = zxcvbn(password)
        results.append({
            "password": password,
            "score": result['score'],
            "crack_time": result['crack_times_display']['offline_slow_hashing_1e4_per_second']
        })
    return results

# Анализ паролей
analysis_results = analyze_passwords(passwords)

# Вывод результатов
for result in analysis_results:
    print(f"Пароль: {result['password']}")
    print(f"Оценка надежности (от 0 до 4): {result['score']}")
    print(f"Время взлома: {result['crack_time']}\n")

# Рекомендации по созданию надежных паролей
recommendations = """
Рекомендации по созданию надежных паролей:
- Используйте длинные пароли (не менее 12 символов).
- Включайте в пароли цифры, заглавные и строчные буквы, а также специальные символы.
- Избегайте использования словарных слов и легко угадываемых комбинаций (например, "123456", "password").
- Не используйте один и тот же пароль для разных учетных записей.
- Регулярно меняйте пароли и используйте менеджер паролей для их хранения.
"""

print(recommendations)
