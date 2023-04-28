# Приложения

Это бэкенд для приложения. Он построен с использованием Django Rest Framework и предоставляет эндпоинты для регистрации пользователей, входа, выхода и двухэтапной регистрации.

## Начало работы

### Предварительные условия

- Python 3.6 или выше
- Docker и Docker Compose (если вы планируете использовать включенный Dockerfile и docker-compose.yaml)

### Установка

1. Клонирование репозитория: `git clone https://github.com/your/repo.git`
2. Установка зависимостей: `pip install -r requirements.txt`
3. Запуск сервера разработки: `python manage.py runserver`

### Запуск с Docker

1. Клонирование репозитория: `git clone https://github.com/your/repo.git`
2. Сборка образа Docker: `docker build -t your-app-name .`
3. Запуск контейнера Docker: `docker-compose up`

## Эндпоинты API

- POST /api/register/: Регистрация нового пользователя. Обязательные поля: username, email, password, confirm_password.
- POST /api/login/: Вход пользователя. Обязательные поля: username, password.
- POST /api/logout/: Выход текущего аутентифицированного пользователя.
- POST /api/registration/first-step/: Завершение первого этапа двухэтапной регистрации. Обязательные поля: first_name, last_name, date_of_birth.
- POST /api/registration/second-step/: Завершение второго этапа двухэтапной регистрации. Обязательное поле: profile_picture.

## Документация API

Документация API доступна через Swagger 3. Вы можете получить доступ к ней, запустив сервер разработки (`python manage.py runserver`) и перейдя по ссылке http://localhost:8000/swagger/.

## Стиль кода

Этот проект использует Flake8 и Black для стиля и форматирования кода. Вы можете проверить нарушения стиля, запустив flake8 и black --check ., соответственно. Чтобы автоматически исправить проблемы со стилем, запустите black ..

## Авторы

Ваше имя your.email@example.com - начальная работа

## Лицензия

Этот проект лицензирован в соответствии с лицензией MIT - подробнее см. в файле LICENSE. 

-----------------------------------------------------------------------------------------------------

# Applications

This is a backend for an application. It is built using Django Rest Framework and provides endpoints for user registration, login, logout, and two-factor registration.

## Getting Started

### Prerequisites

- Python 3.6 or higher
- Docker and Docker Compose (if you plan to use the included Dockerfile and docker-compose.yaml)

### Installation

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Install the dependencies: `pip install -r requirements.txt`
3. Run the development server: `python manage.py runserver`

### Running with Docker

1. Clone the repository: `git clone https://github.com/your/repo.git`
2. Build the Docker image: `docker build -t your-app-name .`
3. Run the Docker container: `docker-compose up`

## API Endpoints

- POST /api/register/: Register a new user. Required fields: username, email, password, confirm_password.
- POST /api/login/: Log in a user. Required fields: username, password.
- POST /api/logout/: Log out the current authenticated user.
- POST /api/registration/first-step/: Complete the first step of two-factor registration. Required fields: first_name, last_name, date_of_birth.
- POST /api/registration/second-step/: Complete the second step of two-factor registration. Required field: profile_picture.

## API Documentation

The API documentation is available through Swagger 3. You can access it by running the development server (`python manage.py runserver`) and navigating to http://localhost:8000/swagger/.

## Code Style

This project uses Flake8 and Black for code style and formatting. You can check for style violations by running `flake8` and `black --check .`, respectively. To automatically fix style issues, run `black ..`.

## Authors

Your Name <your.email@example.com> - Initial work

## License

This project is licensed under the MIT License - see the LICENSE file for details.
