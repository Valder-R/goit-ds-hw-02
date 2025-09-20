from datetime import datetime
import faker
from random import randint, choice
import sqlite3

statuses = [('new',), ('in progress',), ('completed',)]
NUMBER_USERS = 10
NUMBER_TASKS = 100

def generate_fake_data(number_of_users, number_of_tasks) -> tuple:
    fake_users = []
    fake_tasks = []
    fake_data = faker.Faker()
    for _ in range(number_of_users):
        user = tuple([fake_data.name(), fake_data.email()])
        fake_users.append(user)

    for _ in range(number_of_tasks):
        fake_tasks.append(tuple([fake_data.text(max_nb_chars=100), fake_data.text(max_nb_chars=255)]))


    return fake_users, fake_tasks


def prepare_tasks(tasks) -> list:
    for_tasks = []
    for task in tasks:
        for_tasks.append((*task, randint(1,3), randint(1, NUMBER_USERS),))

    return for_tasks


def insert_data(users, tasks, statuses) -> None:
    with sqlite3.connect('tasks.db') as conn:
        cursor = conn.cursor()

        sql_to_status = """INSERT INTO status(name) VALUES (?)"""
        cursor.executemany(sql_to_status, statuses)

        sql_to_users = """INSERT INTO users(fullname, email) VALUES (?, ?)"""
        cursor.executemany(sql_to_users, users)

        sql_to_tasks = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)"""
        cursor.executemany(sql_to_tasks, tasks)

        conn.commit()


if __name__ == '__main__':
    users, tasks = generate_fake_data(NUMBER_USERS, NUMBER_TASKS)
    tasks = prepare_tasks(tasks)
    print(users)
    print(tasks)
    print(statuses)
    insert_data(users, tasks, statuses)