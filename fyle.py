from flask import Flask, request
import json
import psycopg2
import jwt
import datetime

from args import _define_args
from queries import SQL_QUERY

app = Flask(__name__)

ARGS = _define_args()
CONN = psycopg2.connect("dbname = {0} user = {1} host=localhost password={2}"\
.format(ARGS.dbname, ARGS.username, ARGS.password))

cur = CONN.cursor()

@app.route("/api/auth", methods=["POST"])
def auth():
    key = request.json["key"]

    email_id = jwt.decode(key, ARGS.password, algorithms=['HS256'])

    sq_query = SQL_QUERY.get("insert_data", "")

    sq_query = sq_query.format(email_id.get("email", ""))

    try:
        cur.execute(sq_query)
    except psycopg2.errors.UniqueViolation:
        cur.execute("ROLLBACK")
        CONN.commit()
        return (json.dumps({"message": "A user with the email id already exist please generate its key"}))

    CONN.commit()

    return (json.dumps({"message": "Please use {} as key to access apis".format(key)}))

def _get_sql_query(query):
    sq_query = SQL_QUERY.get(query, "")

    return sq_query

@app.route("/api/get_bank_details")
def get_bank_details():

    key = request.args.get("key", "")
    IFSC = request.args.get("ifsc", "")
    IFSC = str(IFSC).upper()

    sq_auth_query = _get_sql_query("auth")

    try:
        email_id = jwt.decode(key, ARGS.password, algorithms=['HS256'])
    except jwt.exceptions.InvalidSignatureError:
        raise Exception("wrong key")
    sq_auth_query = sq_auth_query.format(email_id.get("email", ""))
    cur.execute(sq_auth_query)
    results = cur.fetchall()
    if not results:
        raise Exception("Session expired for this user please regenerate key")

    num = request.args.get("num", 20)
    num = int(num)

    page = int(request.args.get("page", 0))

    start = page*num+1
    end = start + num

    bank_name = str(request.args.get("bank_name", "").replace("_", " "))
    city = str(request.args.get("city", "")).upper()

    if bank_name and city:
        sq_query = _get_sql_query("branch_details")
        sq_query = sq_query.format(bank_name.upper(), city, start, end)
    else:
        sq_query = _get_sql_query("bank_details")

        sq_query = sq_query.format(IFSC, start, end)

    cur.execute(sq_query)

    results = cur.fetchall()

    resp = []
    for result in results:
        _id,ifsc,bank_id,branch,address,city,district,state,bank_name = result

        record = {
                "ifsc": ifsc,
                "bank_id": bank_id,
                "branch": branch,
                "address": address,
                "city": city,
                "district": district,
                "state": state,
                "bank_name": bank_name
                }

        resp.append(record)

    sq_query = SQL_QUERY.get("refresh", "")
    cur.execute(sq_query)
    return json.dumps({"result": resp})

if __name__=="__main__":
    app.run(debug=True, host=ARGS.ip, port=ARGS.port)
