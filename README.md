# Skymarket_SB1

### Контекст

Данная работа представляет собой backend-часть для сайта объявлений. 

Frontend-часть уже готова и находится по адресу https://github.com/skypro-008/coursework_6_skymarket.git


## Описание задач

Бэкенд-часть проекта предполагает реализацию следующего функционала:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту (не обязательно).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

***Старт***

Win -> `python skymarket/manage.py`

Linux -> `python3 skymarket/manage.py`

***ENV***

> Необходимо прописать переменные окружения 
> для подключения к базе данных Postgres:

`POSTGRES_DB`
`POSTGRES_USER`
`POSTGRES_PASSWORD`
`POSTGRES_HOST`
`POSTGRES_PORT`

`SECRET_KEY`

`EMAIL_HOST`
`EMAIL_HOST_USER`
`EMAIL_HOST_PASSWORD`
`EMAIL_PORT`

 Файл `.env` должен находиться в корне проекта.

### В проекте используется Docker Compose

* Установите Docker, следуя инструкциям для вашей операционной
  системы: [Docker Install](https://docs.docker.com/get-docker/).
* Установите Docker Compose: [Docker Compose Install](https://docs.docker.com/compose/install/).

Для запуска приложения необходимо выполнить следующие команды: 
* ***docker-compose build*** - сборка образа
* ***docker-compose up*** - запуск контейнера

Вот пошаговая инструкция:

1. Откройте командную строку или терминал и перейдите в директорию, где находится файл docker-compose.yml.

2. Запустите команду docker-compose up. Docker Compose будет читать файл docker-compose.yml и создавать и запускать контейнеры, описанные в этом файле.

3. По умолчанию, команда docker-compose up будет выводить логи контейнеров в текущем терминале. Чтобы запустить контейнеры в фоновом режиме, используйте флаг -d, например: docker-compose up -d.

4. Docker Compose создаст и запустит все контейнеры, описанные в файле docker-compose.yml. Вы сможете видеть логи работы контейнеров и контролировать их состояние.

5. Чтобы остановить контейнеры, используйте команду docker-compose down. Эта команда остановит и удалит все контейнеры, созданные с помощью docker-compose.yml.