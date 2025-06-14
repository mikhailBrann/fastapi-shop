## переменные виртуального окружения
перед началом сборки проекта необходимо создать файл .env в корне проекта и заполнить его следующими переменными:

```bash
APP_NAME=fast-shop
APP_PORT=8000 # порт на котором будет запущен сервер, у меня 8000 всегда занят просто
POSTGRES_USER=shop_user
POSTGRES_PASSWORD=shop_user
POSTGRES_DB=shop
POSTGRES_HOST=database
```