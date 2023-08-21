from flask import Flask, request, jsonify
from  sub_db_setup import create_table
from flask_cors import CORS

import psycopg2

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:5000"}})

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
        user='admin',
        password='admin123$',
        database='sub_data'
    )
    cursor = connection.cursor()
    cursor.execute("INSERT INTO api_results (operation, num1, num2, result) VALUES (%s, %s, %s, %s);",
                   (operation, num1, num2, result))
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
