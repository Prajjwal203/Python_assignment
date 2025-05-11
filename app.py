from flask import Flask, jsonify
from pymongo import MongoClient


app = Flask(__name__)
client = MongoClient("localhost:27017")

db = client["myDb"]   #database name
users_collection = db["users"]  #collection name

@app.route('/api')
def get_users():
    users = list(users_collection.find({}, {'_id': 0}))
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
 