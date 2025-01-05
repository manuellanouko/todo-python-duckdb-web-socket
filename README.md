# todo-python-duckdb-web-socket

Trying out python duckdb
payments_model: 
    - loads data from a csv file and adds to a table in duck db
payments_server: 
    - starts a new websocket server to search the payments table by payee name, and prints the search results
test_client: 
    - starts a new interactive client that takes in the inputed payee name to search by, sends and it to the server
