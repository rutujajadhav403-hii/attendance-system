from flask import Flask, render_template, request, jsonify
import mysql.connector

app = Flask(__name__)

# ✅ DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Div@4499",   # 🔥 put your MySQL password
    database="attendance_db"
)

# ✅ HOME PAGE
@app.route('/')
def index():
    return render_template('index.html')


# ✅ ADD ATTENDANCE
@app.route('/add', methods=['POST'])
def add():
    data = request.get_json()

    name = data['name']
    roll = data['roll']
    status = data['status']

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO students (name, roll_no, status) VALUES (%s, %s, %s)",
        (name, roll, status)
    )
    db.commit()   # 🔥 VERY IMPORTANT

    cursor.close()

    return jsonify({"message": "Attendance Added"})


# ✅ GET DATA
@app.route('/get', methods=['GET'])
def get_data():
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students ORDER BY id ASC")  # latest on top
    data = cursor.fetchall()

    cursor.close()

    return jsonify(data)


# ✅ CLEAR ALL DATA
@app.route('/clear', methods=['GET'])
def clear():
    cursor = db.cursor()

    cursor.execute("DELETE FROM students")
    db.commit()   # 🔥 VERY IMPORTANT

    cursor.close()

    return jsonify({"message": "All attendance cleared"})


# ✅ RUN SERVER
if __name__ == '__main__':
    app.run(debug=True)