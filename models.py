import sqlite3

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('meals.db')
        self.create_meal_table()

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create_meal_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Meals (
            id INTEGER PRIMARY KEY,
            day TEXT NOT NULL,
            name TEXT NOT NULL,
            ingredients TEXT,
            description TEXT
        );
        """
        self.conn.execute(query)

class MealModel:
    TABLENAME = "Meals"

    def __init__(self):
        self.conn = sqlite3.connect('meals.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        self.conn.commit()
        self.conn.close()

    def create(self, params):
        query = f'INSERT INTO {self.TABLENAME} (day, name, ingredients, description) VALUES (?, ?, ?, ?)'
        self.conn.execute(query, (params.get("day"), params.get("name"), params.get("ingredients"), params.get("description")))
        return self.list_items()

    def update(self, day, update_dict):
        set_query = ", ".join([f'{key} = ?' for key in update_dict.keys()])
        query = f"UPDATE {self.TABLENAME} SET {set_query} WHERE day = ?"
        self.conn.execute(query, (*update_dict.values(), day))
        return self.get_by_day(day)

    def delete(self, day):
        query = f"DELETE FROM {self.TABLENAME} WHERE day = ?"
        self.conn.execute(query, (day,))
        return self.list_items()

    def list_items(self):
        query = f"SELECT * FROM {self.TABLENAME}"
        result_set = self.conn.execute(query).fetchall()
        return [dict(row) for row in result_set]

    def get_by_day(self, day):
        query = f"SELECT * FROM {self.TABLENAME} WHERE day = ?"
        result_set = self.conn.execute(query, (day,)).fetchall()
        return [dict(row) for row in result_set]