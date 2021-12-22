import sqlite3

def create_database(table_name = str):
    """ Creates a floods_data.db """
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    c.execute(f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        date TEXT,
        region TEXT,
        location TEXT,
        main_infrastructure TEXT,
        damaged_infrastructure TEXT,
        water_level REAL,
        image BLOB
    )
    """)
    conn.commit()
    conn.close()


def insert_database(table_name, date, region, location, main_infrastructure, damaged_infrastructure, water_level, image):
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    # Image
    with open(image, "rb") as image_file:
        image = image_file.read()
    c.execute(f"""
    INSERT INTO {table_name} (date, region, location, main_infrastructure, damaged_infrastructure, water_level, image) 
    VALUES (?,?,?,?,?,?,?)""", (date, region, location, main_infrastructure, damaged_infrastructure, water_level, image))
    conn.commit()
    conn.close()

def query_database(table_name):
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    c.execute(f"""
    SELECT * FROM {table_name}
    """)
    result = c.fetchall()
    print(result)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    pass