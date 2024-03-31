import sqlite3

def create_table():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, surname TEXT, name TEXT, phone TEXT, city TEXT)''')
    conn.commit()
    conn.close()

def add_contact(surname, name, phone, city):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (surname, name, phone, city) VALUES (?, ?, ?, ?)", (surname, name, phone, city))
    conn.commit()
    conn.close()

def view_all_contacts():
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    rows = c.fetchall()
    for row in rows:
        print(row)
    conn.close()

def search_contact(surname):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE surname LIKE ?", ('%' + surname + '%',))
    rows = c.fetchall()
    if rows:
        for row in rows:
            print(row)
    else:
        print("Контакт с фамилией '{}' не найден.".format(surname))
    conn.close()

def delete_contact(id):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update_contact(id, new_phone):
    conn = sqlite3.connect('contacts.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET phone=? WHERE id=?", (new_phone, id))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("\nТелефонный справочник")
        print("1. Добавить контакт")
        print("2. Вывести все контакты")
        print("3. Поиск контакта")
        print("4. Удалить контакт")
        print("5. Обновить контакт")
        print("6. Выйти")
        choice = input("Выберите действие: ")

        if choice == "1":
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            phone = input("Введите номер телефона: ")
            city = input("Введите город: ")
            add_contact(surname, name, phone, city)
        elif choice == "2":
            print("\nСписок контактов:")
            view_all_contacts()
        elif choice == "3":
            surname = input("Введите фамилию для поиска: ")
            search_contact(surname)
        elif choice == "4":
            id = input("Введите id для удаления: ")
            delete_contact(id)
        elif choice == "5":
            id = input("Введите id для обновления: ")
            new_phone = input("Введите новый номер телефона: ")
            update_contact(id, new_phone)
        elif choice == "6":
            break
        else:
            print("Некорректный выбор. Пожалуйста, попробуйте еще раз.")

#if __name__ == "__main__":
main()
