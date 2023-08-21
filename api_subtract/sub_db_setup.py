import psycopg2

def create_table():
    connection = psycopg2.connect(
        host='db',
        port='5432',
        user='admin',
        password='admin123$',
        database='sub_data'
    )
    cursor = connection.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS api_results (
            id SERIAL PRIMARY KEY,
            operation VARCHAR(10) NOT NULL,
            num1 FLOAT NOT NULL,
            num2 FLOAT NOT NULL,
            result FLOAT NOT NULL
        );
        """
    )
    connection.commit()
    cursor.close()
    connection.close()
