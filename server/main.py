from flask import Flask, jsonify, request
from flask_cors import CORS
import json, psycopg2, config

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app)

namepass=[]
def RefreshSQL():
    aps=[]
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.db_name    
        )
        print("[INFO] PostgreSQL has succesful connected")
        # the cursor for perfoming database operations
        with connection.cursor() as cursor:
            cursor.execute(
                "select * from users;"
            )
            languages=cursor.fetchall()
            aps=languages
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
    return aps


# sanity check route
@app.route('/api/login', methods=['POST'])
def login():
    namepass=RefreshSQL()
    apr = json.loads(request.data.decode('utf-8'))
    logins = [namepass[i][0] for i in range(len(namepass))]
    if apr['login'] in logins:
        if apr['password'] == namepass[logins.index(apr['login'])][1]:
            return "Good"
        else:
            return "Bad"
    else:
        return "Bad"

@app.route('/api/signup', methods=['POST'])
def signup():
    signuping = request.data
    apr = signuping.decode('utf-8')
    jsp = json.loads(apr)
    try:
        # connect to exist database
        connection = psycopg2.connect(
            host=config.host,
            user=config.user,
            password=config.password,
            database=config.db_name    
        )
        namepass=RefreshSQL()
        print("[INFO] PostgreSQL has succesful connected")
        loginss = [namepass[i][0] for i in range(len(namepass))]
        print(loginss)
        if (jsp['login'] in loginss):
            print("[INFO] User already exists")
            return "Error"
        else: 
            piq = """ INSERT INTO users VALUES (%s,%s)"""
            rti = (jsp['login'], jsp['password'])
            # the cursor for perfoming database operations
            print(piq, rti)
            with connection.cursor() as cursor:
                cursor.execute(piq, rti)
                print("[INFO] User has been registered")
            connection.commit()
            return "User has been registered"
    except Exception as _ex:
            print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            # cursor.close()
            connection.close()
            print("[INFO] PostgreSQL connection closed")
    return "Good"
if __name__ == '__main__':
    app.run()