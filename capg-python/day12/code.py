from pymongo import MongoClient

# 1️⃣ Connect to MongoDB (localhost)
client = MongoClient('mongodb://localhost:27017/')

# 2️⃣ Create or Connect to Database
db = client['cmr']

# 3️⃣ Create or Connect to Collection
collection = db['batch1']

# ------------------ 🔴 CREATE (Insert Data) ------------------
def create_data():
    data = [
        {"name": "Krutin", "age": 25, "city": "Mumbai"},
        {"name": "Alice", "age": 30, "city": "Delhi"},
        {"name": "Bob", "age": 22, "city": "Pune"}
    ]
    result = collection.insert_many(data)
    print("Inserted IDs:", result.inserted_ids)

# ------------------ 🟡 READ (Retrieve Data) ------------------
def read_data():
    print("\nAll Documents:")
    for doc in collection.find():
        print(doc)

# ------------------ 🔵 UPDATE (Modify Data) ------------------
def update_data():
    query = {"name": "Krutin"}
    new_values = {"$set": {"city": "Bangalore"}}
    result = collection.update_one(query, new_values)
    print("\nDocuments Modified:", result.modified_count)

# ------------------ ⚫ DELETE (Remove Data) ------------------
def delete_data():
    query = {"name": "Bob"}
    result = collection.delete_one(query)
    print("\nDocuments Deleted:", result.deleted_count)

# 🚀 Running CRUD Operations
# create_data()
# read_data()
# update_data()
read_data()  # Verify update
delete_data()
read_data()  # Verify deletion
