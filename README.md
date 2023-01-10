# Linked API / Django / Social Network

##### Функционал проекта

* Профиль пользователя
* Аутентификация по JWT
* Кастомная модель пользователя
* Подписчики
* Поиск пользователя
* Галерея фото/видео
* Комментарии
* Лайки
* Личные сообщения между пользователями

---

#### Перед началом работ:

* [Устанавливаем docker]
* [Устанавливаем docker compose]

---

#### Развертывание в терминале

#~ ```docker compose up -d --build``` Сборка и поднятие контейнера

#~ ```docker ps``` Список контейнеров, находим linked_backend

#~ ```docker exec -it linked_backend bash``` подключаемся и открываем терминал

После подключения к контейнеру, мигрируем в бд, django модели

#root@container~ ``` python manage.py migrate ```

Выходим из контейнера

#root@container~ ``` exit ```

Рестартуем!

#~ ```docker compose restart``` Рестарт всех контейнеров

Далее сервис доступен по

[http://localhost:8000](http://localhost:8000)