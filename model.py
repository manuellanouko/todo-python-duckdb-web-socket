import duckdb


def initialise_db():
    # Connect to DB
    con = duckdb.connect("my_trial_db.db")
    # Create todo table
    sql_query = """
        CREATE TABLE IF NOT EXISTS todo (
        id INT NOT NULL PRIMARY KEY,
        title VARCHAR(300) NOT NULL,
        is_done TINYINT NOT NULL DEFAULT 0,
        date_created TIMESTAMP DEFAULT NOW(),
        date_done TIMESTAMP
    )
    """
    con.sql(sql_query)
    # Create a sequence to use to insert the next auto increment value for the todo id 
    sql_query = """
        CREATE SEQUENCE IF NOT EXISTS sequence_todo_id START 1
    """
    con.sql(sql_query)
    # Insert dummy data
    sql_query = """
        INSERT INTO todo (id, title)
        VALUES
            (nextval('sequence_todo_id'), 'hello world'),
            (nextval('sequence_todo_id'), 'Complete trying out duck DB')
    """
    con.sql(sql_query)

    # Close DB connection
    con.close()

def get_all():
    con = duckdb.connect("my_trial_db.db")
    # Select from db
    results = con.sql("FROM todo")
    print(results)
    # Close DB connection
    con.close()

def get(todo_id: int):
    con = duckdb.connect("my_trial_db.db")
    # Select from db
    results = con.sql(f"FROM todo WHERE id={todo_id}")
    # Close DB connection
    con.close()
    print(results)

def add(todo_title: str):
    con = duckdb.connect("my_trial_db.db")
    sql_query = f"""
        INSERT INTO todo (id, title)
        VALUES
            (nextval('sequence_todo_id'), '{todo_title}')
    """
    result = con.sql(sql_query)
    con.close()
    print(result)

def update(todo_id: int, todo_title: str):
    con = duckdb.connect("my_trial_db.db")
    sql_query = f"""
        UPDATE todo 
        SET
            title = '{todo_title}'
        WHERE id = {todo_id}
    """
    result = con.sql(sql_query)
    con.close()
    print(result)

def delete(todo_id: int):
    con = duckdb.connect("my_trial_db.db")
    sql_query = f"""
        DELETE FROM todo
        WHERE id = {todo_id}
    """
    result = con.sql(sql_query)
    con.close()
    print(result)

def complete_todo(todo_id: int):
    con = duckdb.connect("my_trial_db.db")
    sql_query = f"""
        UPDATE todo 
        SET
            is_done = 1
        WHERE id = {todo_id}
    """
    result = con.sql(sql_query)
    con.close()
    print(result)


# initialise_db()
# add("A brand new todo")
# update(3, "Updated: A brand new todo")
# delete(1)
# complete_todo(3)
# get_all()
# get(2)
