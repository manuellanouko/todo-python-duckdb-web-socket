import duckdb


def initialise_db():
    # Connect to DB
    con = duckdb.connect("my_trial_db.db")
    # Create payments table
    sql_query = """CREATE TABLE IF NOT EXISTS payment AS SELECT * FROM payment_information.csv"""
    con.sql(sql_query)
    # Close DB connection
    con.close()

def get_by_name(payee_first_name: str):
    con = duckdb.connect("my_trial_db.db")
    sql_query = f"""
        FROM payment
        WHERE payee_first_name='{payee_first_name}'
    """
    # Select from db
    results = con.sql(sql_query)
    print(results)
    # Close DB connection
    con.close()

# initialise_db()
# get_by_name("Andrea")
