from flask import Flask, request ,jsonify
import mysql.connector
import utilities
import yaml


app = Flask(__name__)


db = yaml.load(open('db.yaml'), Loader=yaml.FullLoader)

# ------------------------------ API start ------------------------------#
@app.route('/')
def homepage():
    return """
    Hello world!
    
    This is my first web app!

    I'm so excited!
    """,200

@app.route('/signup',methods = ['POST'])
def SignupHandler():
    data = request.json
    try:
        try:
            connection,cursor = utilities.ConnectToDatabase(db)
            cursor.execute("INSERT INTO user(Username,Pass,Email) VALUES(%s,%s,%s)",(data['username'],data['password'],data['email']))
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({"status": "Success"}),201

        except mysql.connector.Error as error:
            return jsonify({"status": format(error)}),500
    except Exception as error:
        return jsonify({"status": repr(error)}),400


@app.route('/login',methods = ['POST'])
def LoginHandler():
    data = request.json
    Key = list(data.keys())[0]
    try:
        try:
            connection,cursor = utilities.ConnectToDatabase(db)
            sql = "SELECT * FROM user WHERE {} = %s".format(Key)
            cursor.execute(sql,(data[Key],))
            result = cursor.fetchone()
            if result is not None:
                if data['password'] == result[1]:
                    return jsonify({"status": "logged In"}),200
                else:
                    return jsonify({"status": "Password is not correct"}),400
            else:
                return jsonify({"status": "Username or email is not correct"}),400
        except mysql.connector.Error as error:
            return jsonify({"status": format(error)}),500

    except Exception as error:
        return jsonify({"status": repr(error)}),400


@app.route('/insert-numbers',methods = ['POST'])
def InsertNumbersHandler():
    data = request.json
    numbers = data['numbers'];
    try:
        for i in range(len(numbers)):
            numbers[i] = (numbers[i],)
        try:
            connection,cursor = utilities.ConnectToDatabase(db)
            sql = """INSERT INTO numbers(TestNumber) VALUES (%s) """
            cursor.executemany(sql, numbers)
            connection.commit()
            cursor.close()
            connection.close()
            return jsonify({"status": "Posted :)"}),201
        except mysql.connector.Error as error:
            return jsonify({"status": format(error)}),500
    except Exception as error:
        return jsonify({"status": repr(error)}),400


@app.route('/show-numbers',methods = ['GET'])
def showNumbersHandler():
    try:
        try:
            connection,cursor = utilities.ConnectToDatabase(db)
            sql_select_Query = "select * from numbers"
            cursor = connection.cursor()
            cursor.execute(sql_select_Query)
            result = cursor.fetchall()
            for i in range(len(result)):
                result[i] = result[i][0]
            cursor.close()
            connection.close()

            return jsonify(numbers = result),200

        except mysql.connector.Error as error:
            return jsonify({"status": format(error)}),500

    except Exception as error:
        return jsonify({"status": repr(error)}),400

@app.route('/delete-numbers',methods = ['DELETE'])
def DeleteNumbersHandler():
    try:
        try:
            connection,cursor = utilities.ConnectToDatabase(db)
            sql = """DELETE FROM numbers"""
            cursor.execute(sql)
            connection.commit()
            cursor.close()
            connection.close()

            return jsonify({"status" : "Deleted :)"}),201

        except mysql.connector.Error as error:
            return jsonify({"status": format(error)}),500

    except Exception as error:
        return jsonify({"status": repr(error)}),400

if __name__ == "__main__":
    app.run(debug=True) # development