import sys

import pytest


def run_tests():
    pytest_args = [
        '--maxfail=1',  # Ограничить количество неудачных тестов
        '--disable-warnings',  # Отключить предупреждения
        '--tb=short',  # Указать формат отчета о тестах (короткий)
        '--capture=no',  # Отключить захват вывода во время тестов (для отладки)
    ]

    result = pytest.main(pytest_args)

    if result != 0:
        print(f"Some tests failed with status code: {result}")
        sys.exit(result)
    else:
        print("All tests passed successfully.")

if __name__ == "__main__":
    run_tests()