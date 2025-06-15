## переменные виртуального окружения
перед началом сборки проекта необходимо создать файл .env в корне проекта и заполнить его следующими переменными:

```bash
APP_NAME=fast-shop
APP_PORT=8000 # порт на котором будет запущен сервер, у меня 8000 всегда занят просто
POSTGRES_USER=shop_user
POSTGRES_PASSWORD=shop_user
POSTGRES_DB=shop
POSTGRES_HOST=database
ACCESS_API_LOGIN=api-login # логин для доступа к api
ACCESS_API_PASSWORD=api-password # пароль для доступа к api
SECRET_API_KEY=access_token_secret # секретный ключ для генерации токена
```

## инициализация таблиц в базе данных
производится через эндпоинт

```bash
POST /setup_db
```
сделал для удобства разработки, позже перенесу в миграции

## получение токена для доступа к api

```bash
POST /auth/get_token

{
  "login": "string", # логин для доступа к api ACCESS_API_LOGIN (.env)
  "password": "string" # пароль для доступа к api ACCESS_API_PASSWORD (.env)
}
```

## документация api
документация api доступна по адресу /docs