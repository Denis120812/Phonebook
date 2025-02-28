# **Телефонный справочник**

### **Описание задачи.**
Создать консольное приложение Телефонный справочник с внешним хранилищем информации и основным функционалом - просмотр, сохранение, импорт, поиск, удаление, изменение данных.

Дедлайн: до 13:30 02.04.2024

Автор: Шестаков Денис - https://github.com/Denis120812/

## **О проекте**

Этот скрипт на Python предоставляет простую систему управления телефонным справочником. Пользователи могут выполнять различные операции, такие как добавление контактов, просмотр всех контактов, поиск контактов, удаление контактов, обновление контактов и импорт контактов из файлов CSV.

## **Предварительные требования**

Для запуска проекта в VCS требуется установить:
- Python 3.x
- SQLite3
- EasyGUI (pip install easygui)
- Tabulate (pip install tabulate)


**Как запустить проект** (рекомендую использовать VCS)

Для запуска с помощью консоли:
1. скачать проект в локальный репозиторий;
2. открыть в VCS папку с проектом (в папке должны находится все скачанные файлы проекта);
3. запустить файл phonebook.py;
4. запустить код кнопкой RUN;
5. выберите нужное действие из представленного меню с помощью диалогов EasyGUI.

## **Доступные действия:**
1. Вывести все контакты: Отображает все контакты, сохраненные в телефонной книге.
2. Добавить контакт: Позволяет пользователю добавить новый контакт, указав фамилию, имя, номер телефона и город. (ID присваивается автоматически при добавлении контакта и является уникальным)
3. Поиск контакта: Поиск контакта по фамилии.
4. Удалить контакт: Удаляет контакт по его ID.
5. Обновить контакт: Обновляет номер телефона контакта по его ID.
6. Импорт контакта: Позволяет импортировать контакты из файлов CSV. Пользователи могут выбрать импорт одного контакта по ID или импорт всех контактов из файла CSV.
7. Выход: Закрывает приложение.



