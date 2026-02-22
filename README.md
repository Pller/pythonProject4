Проект для управления товарами и категориями в интернет-магазине. Реализованы основные классы для работы с продуктами и категориями, включая магические методы.

## Структура проекта
pythonProject3/
├── src/ # Исходный код
│ ├── init.py
│ ├── product.py # Класс Product
│ ├── category.py # Класс Category
│ └── iter_category.py # Класс CategoryIterator (дополнительно)
├── tests/ # Тесты
│ ├── init.py
│ ├── test_product.py
│ ├── test_category.py
│ └── test_iter_category.py
├── main.py # Основной файл
├── requirements.txt # Зависимости
├── .coveragerc # Конфигурация coverage
├── .flake8 # Конфигурация flake8
└── README.md # Документация

## Установка

### 1. Клонирование репозитория

git clone <repository-url>
cd pythonProject3
2. Создание виртуального окружения

# Для Windows
python -m venv venv
venv\Scripts\activate

# Для Linux/Mac
python3 -m venv venv
source venv/bin/activate
3. Установка зависимостей

pip install -r requirements.txt