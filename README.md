# Django CRUD API с PostgreSQL и Docker

## Описание проекта

Этот проект представляет собой **CRUD API** для управления пользователями. Реализован на **Django** с использованием базы данных **PostgreSQL**. Сборка и запуск выполнены с помощью **Docker** и **docker-compose**.

---

## **Функционал**

1. **Создание пользователя**:
   - Метод: `POST`
   - URL: `/api/users/`
2. **Получение данных пользователя по ID**:
   - Метод: `GET`
   - URL: `/api/users/{id}/`
3. **Обновление пользователя**:
   - Метод: `PUT`
   - URL: `/api/users/{id}/update/`
4. **Удаление пользователя**:
   - Метод: `DELETE`
   - URL: `/api/users/{id}/delete/`

---

## **Технологии**

- Python 3.10
- Django 3.2
- PostgreSQL 15
- Docker и Docker Compose
- Python-dotenv (для работы с переменными окружения)

---

## **Как запустить проект локально?**

### **1. Клонируйте репозиторий**

```bash
git clone git@github.com:BillyMilligan1207/user_crud_project.git
cd user_crud_project
