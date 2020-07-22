
# ----- Example Python program to create a database in PostgreSQL using Psycopg2 -----

# import the PostgreSQL client for Python

import psycopg2
import tkinter as tk

from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

 

# Connect to PostgreSQL DBMS

con = psycopg2.connect("user=postgres password='your_password'");

con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT);

 

# Obtain a DB Cursor

cursor          = con.cursor();

name_Database   = "AppStore";

 

# Create table statement

sqlCreateDatabase = "create database "+name_Database+";"

 

# Create a table in PostgreSQL database

try:
    cursor.execute(sqlCreateDatabase);
except psycopg2.errors.DuplicateDatabase:
    print("Duplicate DB => pass")

try:
    with open('full_creator.sql') as cfile:
        cursor.execute(cfile.read())
except psycopg2.errors.DuplicateTable:
    print("Dup relation => pass")

try:
    with open('full_populator.sql') as pfile:
        cursor.execute(pfile.read())
except psycopg2.errors.UniqueViolation:
    print("Dup entry => pass")

def exec_select(st):
    cursor.execute(st)
    res = []
    row = cursor.fetchone()
    while row is not None:
        res.append(str(row))
        row = cursor.fetchone()
    return res

def query(i):
    q = None
    if (i == 1):
        q = """
        SELECT
            apt.id, display_name, date_created
        FROM
            "Apps" AS apt
            LEFT JOIN "Uploads" AS upt ON apt.id = upt.id
        ORDER BY
            date_created DESC
        LIMIT 20
        """
    elif (i == 2):
        q = """
        SELECT
            display_name
        FROM
            "Apps" AS apt
            LEFT JOIN "Downloads" AS dt ON apt.package_id = dt.package_id
        WHERE
            user_id = 5
        """
    elif (i == 3):
        q = """
        SELECT
            user_id,
            package_id,
            rate,
            text
        FROM ("Reviews" AS rt
            LEFT JOIN "Users" AS ut ON rt.user_id = ut.id)
        WHERE
            user_id = 3
        """
    elif (i == 4):
        q = """
        SELECT
            display_name
        FROM
            "Apps" AS apt
            LEFT JOIN "Packages" AS pt ON apt.package_id = pt.id
        WHERE
            dev_id IN (
                SELECT
                    id
                FROM
                    "Developers" AS dt
                WHERE
                    dt.first_name = 'David'
                    AND dt.last_name = 'RICHARDSON')
        """
    elif (i == 5):
        q = """
        SELECT
            sum(price) AS TotalSum
        FROM
            "Payments" AS payt
            LEFT JOIN "Purchases" AS purt ON payt.purchase_id = purt.id
        WHERE
            package_id IN (
                SELECT
                    package_id
                FROM
                    "Packages"
                WHERE
                    dev_id = 2)
        """
    elif (i == 6):
        q = """
        SELECT
            user_id,
            date_created
        FROM
            "Downloads"
        WHERE
            package_id = 335
            AND date_created BETWEEN NOW()::date - EXTRACT(DOW FROM NOW())::integer - 7
            AND NOW()::date - EXTRACT(DOW FROM NOW())::integer
        """
    elif (i == 7):
        q = """
        SELECT
            id
        FROM
            "Users"
        WHERE
            id IN (
                SELECT
                    user_id
                FROM
                    "Purchases")
        """
    elif (i == 8):
        q = """
        SELECT
            *
        FROM
            "Reviews"
        WHERE
            package_id = 12
            AND date_created BETWEEN NOW()::date - EXTRACT(DOW FROM NOW())::integer - 7
            AND NOW()::date - EXTRACT(DOW FROM NOW())::integer
        """
    elif (i == 9):
        q = """
        SELECT
            *
        FROM
            "Users"
        WHERE
            first_name LIKE '%Jack%'
        """
    elif (i == 10):
        q = """
        SELECT
            package_id
        FROM
            "Reviews"
        GROUP BY
            package_id
        ORDER BY
            avg(rate) ASC
        """
    elif (i == 11):
        q = """
        SELECT
            sum(price) AS TotalPaid
        FROM
            "Purchases" AS purt
            LEFT JOIN "Payments" AS payt ON purt.id = payt.purchase_id
        WHERE
            package_id IN (
                SELECT
                    package_id
                FROM
                    "Packages"
                WHERE
                    dev_id = 1)
            AND date_completed BETWEEN NOW()::date - EXTRACT(DOW FROM NOW())::integer - 30
            AND NOW()::date - EXTRACT(DOW FROM NOW())::integer
        """
    elif (i == 12):
        q = """
        SELECT
            *
        FROM
            "Users"
        WHERE
            id NOT IN ( SELECT DISTINCT
                    user_id
                FROM
                    "Downloads"
                WHERE
                    package_id IN (
                        SELECT
                            package_id
                        FROM
                            "Apps"
                        WHERE
                            display_name = 'Telegram')
                        AND date_created BETWEEN NOW()::date - EXTRACT(DOW FROM NOW())::integer - 365
                        AND NOW()::date - EXTRACT(DOW FROM NOW())::integer)
        """
    elif (i == 13):
        q = """
        SELECT
            *
        FROM
            "Games"
        WHERE
            display_name LIKE '%Clash Of%'
        """
    elif (i == 14):
        q = """
        SELECT
            user_id,
            sum(price) AS TotalPaid
        FROM
            "Purchases" AS purt
            LEFT JOIN "Payments" AS payt ON (purt.id = payt.purchase_id
                    AND purt.type = '1')
        WHERE
            package_id IN (
                SELECT
                    package_id
                FROM
                    "Games"
                WHERE
                    display_name = 'Clash Of Clans')
        GROUP BY
            user_id
        ORDER BY
            TotalPaid DESC
        LIMIT 10
        """
    elif (i == 15):
        q = """
        SELECT
            user_id,
            rate,
            text
        FROM ("Reviews" AS rt
            LEFT JOIN "Users" AS ut ON rt.user_id = ut.id) AS urt
            LEFT JOIN "Games" AS apt ON urt.package_id = apt.package_id
        WHERE
            display_name = 'Clash Of Titans'
        """
    elif (i == 16):
        q = """
        UPDATE
            "Reviews"
        SET
            text = 'This is the next text'
        WHERE
            id = 12
        """
    elif (i == 17):
        q = """
        SELECT
            package_id, avg(rate)
        FROM
            "Reviews"
        GROUP BY
            package_id
        ORDER BY
            avg(rate) DESC
        LIMIT 100
        """
    elif (i == 18):
        q = """
        SELECT
            *
        FROM
            "Developers"
        WHERE
            email LIKE '%gmail.com'
        """
    elif (i == 19):
        q = """
        SELECT
            name AS CategoryName,
            count(package_id) AS NumberOfApps
        FROM
            "Apps" AS apt
            LEFT JOIN "Categories" AS ct ON apt.category_id = ct.id
        GROUP BY
            name
        """
    if (q is None):
        print("Invalid Query")
    else:
        res = exec_select(q)
        print("Success")
        return "\n".join(res)

def handle_click(event):
    print("The button was clicked!")
    q = entry.get()
    print(q)
    ind = int(q)
    if (ind > 0 and ind < 20):
        text_result.delete(1.0, "end")
        text_result.insert(1.0, query(ind))

window = tk.Tk()
greeting = tk.Label(text="App Store Database Test App")
greeting.pack()
query_label = tk.Label(text="Enter your query number in the text field and press enter:")
query_label.pack()
entry_header = tk.Label(text="Query Number:")
entry = tk.Entry(width=50)
button = tk.Button(
    text="Execute Query",
    width=25,
    height=5,
)
entry_header.pack()
entry.pack()
button.pack()
text_result = tk.Text()
text_result.pack()
button.bind("<Button-1>", handle_click)
window.mainloop()
