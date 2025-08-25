import sqlite3

DB_NAME = "patients.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            gender TEXT,
            blood_group TEXT,
            mobile TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS health_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_id INTEGER,
            ambient_temp REAL,
            object_temp REAL,
            bpm REAL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(patient_id) REFERENCES patients(id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_patient(name, age, gender, blood_group, mobile):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO patients (name, age, gender, blood_group, mobile)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, age, gender, blood_group, mobile))
    conn.commit()
    conn.close()

def insert_health_data(patient_id, ambient_temp, object_temp, bpm):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO health_data (patient_id, ambient_temp, object_temp, bpm)
        VALUES (?, ?, ?, ?)
    ''', (patient_id, ambient_temp, object_temp, bpm))
    conn.commit()
    conn.close()

# Call init_db() when the app starts
init_db()
