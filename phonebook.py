
import sqlite3
import csv
import easygui as eg
from tabulate import tabulate

def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, 
              surname TEXT,
               name TEXT, phone INTEGER, city TEXT)''')
    conn.commit()
    conn.close()

def add_contact(surname, name, phone, city): 
    if not surname or not name or not phone or not city:
        eg.msgbox("Все поля должны быть заполнены.", "Ошибка добавления")
        return
    if not phone.isdigit():
        eg.msgbox("Номер телефона должен содержать только цифры.", "Ошибка добавления")
        return
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (surname, name, phone, city) VALUES (?, ?, ?, ?)", (surname, name, phone, city))
    conn.commit()
    conn.close()
    eg.msgbox("Контакт успешно добавлен.", "Добавление")

def view_all_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    conn.close()

    if rows:
        headers = ["ID", "Surname", "Name", "Phone", "City"]
        table = tabulate(rows, headers=headers, tablefmt="grid")
        eg.msgbox(table)
    else:
        eg.msgbox("Список контактов пуст.")


def search_contact(surname):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE surname LIKE ?", ('%' + surname + '%',))
    rows = c.fetchall()
    if rows:
        headers = ["ID", "Surname", "Name", "Phone", "City"]
        table = tabulate(rows, headers=headers, tablefmt="grid")
        eg.msgbox(table)
    else:
        eg.msgbox("Контакт с фамилией '{}' не найден.".format(surname), title="Результаты поиска")
    conn.close()

    
def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (id,))
    rows_deleted = c.rowcount
    conn.commit()
    conn.close()

    if rows_deleted == 1:
        eg.msgbox("Контакт успешно удален.", "Удаление", ok_button="OK")
    else:
        eg.msgbox("Контакт с ID {} не найден в базе данных.".format(id), "Ошибка удаления", ok_button="OK")


def update_contact(id, new_phone):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

# Проверяем, существует ли контакт с заданным ID
    c.execute("SELECT * FROM contacts WHERE id=?", (id,))
    contact = c.fetchone()
    conn.close()
    
    if contact is None:
        eg.msgbox("Контакт с ID {} не найден в базе данных.".format(id), "Ошибка обновления", ok_button="OK")
        return
    
    if not new_phone.isdigit():
        eg.msgbox("Номер телефона должен содержать только цифры.", "Ошибка добавления", ok_button="OK")
        return
    
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET phone=? WHERE id=?", (new_phone, id))
    conn.commit()
    conn.close()
    eg.msgbox("Контакт успешно изменен.", "Изменение данных", ok_button="OK")

def import_single_contact_from_csv(id, csv_file):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            if row[0] == id:
                surname, name, phone, city = row[1:]
                c.execute("INSERT INTO contacts (surname, name, phone, city) VALUES (?, ?, ?, ?)",
                          (surname, name, phone, city))
                eg.msgbox("Контакт успешно импортирован из файла {}".format(csv_file), title="Импорт контакта", ok_button="OK")
                break
        else:
            eg.msgbox("Контакт с id '{}' не найден в файле".format(id), title="Импорт контакта", ok_button="OK")

    conn.commit()
    conn.close()

def import_all_contacts_from_csv(csv_file):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()

    with open(csv_file, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Пропускаем заголовок, если он есть
        for row in csv_reader:
            surname, name, phone, city = row
            c.execute("INSERT INTO contacts (surname, name, phone, city) VALUES (?, ?, ?, ?)",
                      (surname, name, phone, city))

    conn.commit()
    conn.close()
    eg.msgbox("Все контакты успешно импортированы из файла {}".format(csv_file), title="Импорт контактов", ok_button="OK")

def main():
    create_table()
    while True:
        choice = eg.choicebox("Выберите действие:", title="Телефонный справочник", choices=["Вывести все контакты", 
        "Добавить контакт", "Поиск контакта", "Удалить контакт", "Изменить контакт", "Импорт контакта", "Выйти"])

        if choice == "Вывести все контакты":
            view_all_contacts()
        elif choice == "Добавить контакт":
            surname = eg.enterbox("Введите фамилию:")
            name = eg.enterbox("Введите имя:")
            phone = eg.enterbox("Введите номер телефона:")
            city = eg.enterbox("Введите город:")
            add_contact(surname, name, phone, city)
            
        elif choice == "Поиск контакта":
            surname = eg.enterbox("Введите фамилию для поиска:")
            search_contact(surname)
        elif choice == "Удалить контакт":
            id = eg.enterbox("Введите id контакта для удаления:")
            delete_contact(id)
        elif choice == "Изменить контакт":
            id = eg.enterbox("Введите id контакта для изменения:")
            new_phone = eg.enterbox("Введите новый номер телефона:")
            update_contact(id, new_phone)
        elif choice == "Импорт контакта":
            import_choice = eg.choicebox("Выберите способ импорта:", choices=["Импорт одного контакта по ID", "Импорт всех контактов"])
            if import_choice == "Импорт одного контакта по ID":
                contact_id = eg.enterbox("Введите ID контакта:")
                csv_file = eg.fileopenbox("Выберите CSV файл для импорта:")
                import_single_contact_from_csv(contact_id, csv_file)
            elif import_choice == "Импорт всех контактов":
                csv_file = eg.fileopenbox("Выберите CSV файл для импорта:")
                import_all_contacts_from_csv(csv_file)
        elif choice == "Выйти":
            break
        else:
            eg.msgbox("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

main()



