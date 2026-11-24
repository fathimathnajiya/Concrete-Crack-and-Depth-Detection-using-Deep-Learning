import sqlite3

con = sqlite3.connect("database.db")
con.executescript("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT,
    role INTEGER, name TEXT, dob TEXT, email TEXT, contact TEXT,
    address TEXT, gender TEXT, img TEXT);
CREATE TABLE IF NOT EXISTS reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT, project_id INTEGER, user_id INTEGER,
    review_text TEXT, date_time TEXT);
CREATE TABLE IF NOT EXISTS prediction (
    id INTEGER PRIMARY KEY AUTOINCREMENT, userid INTEGER, pred_result TEXT,
    pred_image TEXT, orginal_image TEXT, avg_depths TEXT, confidence REAL,
    date_time TEXT);
CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT, pcat TEXT, pname TEXT, ptype TEXT,
    duration TEXT, area TEXT, client TEXT, location TEXT, bheight TEXT,
    ftype TEXT, fmaterial TEXT, pspace TEXT, erate TEXT, sdesc TEXT,
    poverview TEXT, status TEXT, img TEXT);
""")
con.commit()
con.close()
print("Database created.")
