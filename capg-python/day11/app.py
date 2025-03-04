from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="cmr_batch1"
    )


@app.route('/employees', methods=['POST'])
def create_employee():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO employees (name, email, address) VALUES (%s, %s, %s)", (name, email, address))
    conn.commit()

    employee_id = cursor.lastrowid
    cursor.close()
    conn.close()

    return jsonify({"message": "Employee created successfully", "id": employee_id}), 201


@app.route('/employees', methods=['GET'])
def get_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    employee_list = [{"id": emp[0], "name": emp[1], "email": emp[2], "address": emp[3]} for emp in employees]

    cursor.close()
    conn.close()

    return jsonify(employee_list), 200

@app.route('/employees/<int:employee_id>', methods=['GET'])
def get_employee(employee_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = %s", (employee_id,))
    employee = cursor.fetchone()

    cursor.close()
    conn.close()

    if employee:
        return jsonify({"id": employee[0], "name": employee[1], "email": employee[2], "address": employee[3]}), 200
    else:
        return jsonify({"error": "Employee not found"}), 404

@app.route('/employees/<int:employee_id>', methods=['PUT'])
def update_employee(employee_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    address = data.get('address')

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE employees SET name = %s, email = %s, address = %s WHERE id = %s", 
                   (name, email, address, employee_id))
    conn.commit()

    if cursor.rowcount == 0:
        cursor.close()
        conn.close()
        return jsonify({"error": "Employee not found"}), 404

    cursor.close()
    conn.close()

    return jsonify({"message": "Employee updated successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
