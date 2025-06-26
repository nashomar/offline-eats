from flask import Flask, request, jsonify
from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
from couchbase.collection import InsertOptions
from couchbase.management.queries import CreatePrimaryIndexQuery
import uuid

# --- CONFIG ---
COUCHBASE_ENDPOINT = "couchbases://cb.n5pqakjxaq311obq.cloud.couchbase.com"
COUCHBASE_BUCKET = "offlineeats"
USERNAME = "offlineeats-user"     # Replace with your actual DB username
PASSWORD = "YourSecurePassword"   # Replace with your actual DB password

# --- INIT APP ---
app = Flask(__name__)

# --- INIT COUCHBASE ---
try:
    cluster = Cluster(
        COUCHBASE_ENDPOINT,
        ClusterOptions(PasswordAuthenticator(USERNAME, PASSWORD))
    )
    bucket = cluster.bucket(COUCHBASE_BUCKET)
    bucket.on_connect()
    collection = bucket.default_collection()
except CouchbaseException as e:
    print("Error connecting to Couchbase:", e)

# --- ROUTES ---

@app.route("/")
def index():
    return "✅ OfflineEats backend is running and connected to Couchbase!"

@app.route("/add-food", methods=["POST"])
def add_food():
    try:
        data = reque
