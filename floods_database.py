import sqlite3

def create_database() -> None:
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    conn.commit()
    conn.close()


def create_table(table_name) -> None:
    """ Creates a floods_data.db and a table specified by its region. """
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


def insert_table(table_name, date, region, location, main_infrastructure, damaged_infrastructure, water_level, image) -> None:
    """ Inserts new data in floods_data.db on the table it is specified to be on. """ 
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    # Image
    with open(image, "rb") as image_file:
        image = image_file.read()
    c.execute(f"""
    INSERT INTO {table_name} (
        date, 
        region, 
        location, 
        main_infrastructure, 
        damaged_infrastructure, 
        water_level, 
        image
        ) 
    VALUES (?,?,?,?,?,?,?)""", (
        date, 
        region, 
        location, 
        main_infrastructure, 
        damaged_infrastructure, 
        water_level, 
        image
        )
    )
    conn.commit()
    conn.close()

def query_table(table_name, *columns, **filters) -> dict:
    """ Gathers data from the specified table name from floods_data.db"""
    conn = sqlite3.connect("floods_data.db")
    c = conn.cursor()
    results = {column: [] for column in columns}
    clauses = " ".join([f"{clause} {condition}" for clause, condition in filters.items()])
    for column in columns:
        c.execute(f"""
        SELECT {column} FROM {table_name} {clauses}
        """)
        for data in c.fetchall():
            results[column].append(data[0])
    conn.commit()
    conn.close()
    return results

# def query_table_list() -> None:
#     conn = sqlite3.connect("floods_data.db")
#     c = conn.cursor()
#     c.execute(f"""
#     SELECT name FROM sqlite_master WHERE type='table';
#     """)
#     table_list = [result[0] for result in c.fetchall()]
#     # print(table_list)
#     return table_list


if __name__ == "__main__":
    # create_database()
    print(query_table("sqlite_master", "name", WHERE="type='table'"))
    # query_table("national_capital_region", "location", "water_level")
    # print(query_table("national_capital_region", "date", WHERE="location=='Quezon City'"))