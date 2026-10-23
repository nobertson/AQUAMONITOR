import sqlite3


class Storage:
    def __init__(self, path="aqua.db"):
        self.conn = sqlite3.connect(path)
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                temperature_c REAL, ph REAL,
                dissolved_oxygen_mg_l REAL, turbidity_ntu REAL)"""
        )
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS alerts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT NOT NULL,
                message TEXT NOT NULL)"""
        )
        self.conn.commit()

    def save_reading(self, r: dict):
        self.conn.execute(
            "INSERT INTO readings (timestamp, temperature_c, ph, "
            "dissolved_oxygen_mg_l, turbidity_ntu) VALUES (?, ?, ?, ?, ?)",
            (r["timestamp"], r["temperature_c"], r["ph"],
             r["dissolved_oxygen_mg_l"], r["turbidity_ntu"]),
        )
        self.conn.commit()

    def save_alert(self, timestamp: str, message: str):
        self.conn.execute(
            "INSERT INTO alerts (timestamp, message) VALUES (?, ?)",
            (timestamp, message),
        )
        self.conn.commit()

    def close(self):
        self.conn.close()
        