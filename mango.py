from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Change if using Atlas
db = client["todo_db"]
collection = db["todo_items"]

@app.route("/submittodoitem", methods=["POST"])
def submit_todo_item():
    data = request.get_json()

    # Extract fields from request body
    item_name = data.get("itemName")
    item_description = data.get("itemDescription")

    # Validate input
    if not item_name or not item_description:
        return jsonify({"error": "itemName and itemDescription are required"}), 400

    # Document to insert
    todo_document = {
        "itemName": item_name,
        "itemDescription": item_description
    }

    # Insert into MongoDB
    result = collection.insert_one(todo_document)

    return jsonify({
        "message": "Item saved successfully",
        "inserted_id": str(result.inserted_id)
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
def hello_world():
    return "hello, world"   
