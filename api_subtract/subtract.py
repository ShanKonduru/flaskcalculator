from flask import Flask, request, jsonify
from  db_setup import create_table
from flask_cors import CORS

import psycopg2

app = Flask(__name__)
CORS(app, origins="http://localhost:8080")

# Call the create_table function before starting the API
create_table()

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    num1 = data['num1']
    num2 = data['num2']
    result = num1 - num2
    save_to_db('Subtract', num1, num2, result)
    return jsonify({"result": result})

def save_to_db(operation, num1, num2, result):
    connection = psycopg2.connect(
        host='db',
        port='5432',
        user='postgres',
        password='example_password',
        database='api_data'
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO api_results (operation, num1, num2, result) VALUES (%s, %s, %s, %s);",
                   (operation, num1, num2, result))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
