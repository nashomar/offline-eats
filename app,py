from flask import Flask, request, jsonify
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.collection import InsertOptions
import uuid

app = Flask(__name__)

# 🔐 Replace with your real connection details
COUCHBASE_ENDPOINT = "couchbases://your-cluster.cloud.couchbase.com"
COUCHBASE_BUCKET = "offlineeats"
USERNAME = "offlineeats-user"
PASSWORD = "your-password"

cluster = Cluster(
    COUCHBASE_ENDPOINT,
    ClusterOptions(PasswordAuthenticator(USERNAME, PASSWORD))
)
bucket = cluster.bucket(COUCHBASE_BUCKET)
collection = bucket.default_collection()

@app.route('/')
def hello():
    return "Hello from OfflineEats + Couchbase!"

@app.route('/add-food', methods=['POST'])
def add_food():
    data = request.json
    food = data.get("food")
    if not food:
        return jsonify({"error": "Missing food item"}), 400

    doc_id = f"food::{uuid.uuid4()}"
    collection.insert(doc_id, {"name": food})
    return jsonify({"message": "Food saved!", "id":
