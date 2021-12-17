from flask import Flask, request, jsonify

import sqlite3



app = Flask(__name__)

def initiateDB():
  DBconn = sqlite3.connect('database.db')
  DBcursor = DBconn.cursor()
  return DBconn, DBcursor

@app.route('/',methods=["GET"])
def default():
  DBconn,DBcursor = initiateDB()
  DBcursor.execute('''CREATE TABLE IF NOT EXISTS skincare (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name data_type TEXT,
                    brand data_type TEXT,
                    type data_type TEXT
                  );
                  ''')
  # DBconn.execute('INSERT INTO skincare (name, brand, type)  VALUES ("Daily Facial Cleanser", "CETAPHIL", "Face Wash")')
  DBconn.commit()
  DBconn.close()
  return '[GET] /listSkincareRutinku \n\n [POST] /skinCareRutin'

@app.route('/listSkincareRutinku',methods=["GET"])
def list():
    DBconn,DBcursor = initiateDB()
    SQL = "SELECT * FROM skincare"
    DBcursor.execute(SQL)
    DBconn.commit()
    products = []
    for row in DBcursor:
      products.append(row)
    DBconn.close()
    return jsonify(products)

@app.route('/skinCareRutinku',methods=["POST"])
def create():
  request_data = request.json

  nama = request_data["nama"]
  merk = request_data["merk"]
  jenis = request_data["jenis"]
  
  DBconn,DBcursor = initiateDB()
  SQL = "INSERT INTO skincare (name, brand, type) VALUES (?, ?, ?)"
  DBcursor.execute(SQL, nama, merk, jenis)
  DBconn.commit()
  result = {"message": "record created"}
  DBconn.close()
  return result


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=80)