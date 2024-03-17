from flask import Flask, request, render_template, redirect, jsonify
import os
import mysql.connector as mysql

app = Flask(__name__)

conn = mysql.connect(
    host="localhost",
    user="root",
    password="Boat2547",
    port=3306,
    database="my_memo"
)

@app.route('/put_user', methods=['PUT'])
def put_user():
    response = request.get_json()

    idmemo = response['idmemo']
    firstname = response['firstname']
    lastname = response['lastname']
    email = response['email']

    conn.reconnect()
    cur = conn.cursor()
    sql = "UPDATE memo SET firstname=%s, lastname=%s, email=%s WHERE idmemo=%s"
    data = (firstname, lastname, email, idmemo)
    cur.execute(sql, data)
    conn.commit()
    conn.close()
    return redirect('http://10.60.7.36:5001/getuser')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5004, debug=True)