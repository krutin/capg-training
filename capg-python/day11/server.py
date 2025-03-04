from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database (In-memory)
items = {}

# Create Item
@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json()
    item_id = data.get('id')
    name = data.get('name')
    
    if item_id in items:
        return jsonify({"error": "Item with this ID already exists"}), 400
    
    items[item_id] = {'name': name}
    return jsonify({"message": "Item created successfully", "item": items[item_id]}), 201

# Get All Items
@app.route('/items', methods=['GET'])
def get_all_items():
    if not items:
        return jsonify({"message": "No items found"}), 200
    
    return jsonify(items), 200


# Read Item
@app.route('/items/<int:item_id>', methods=['GET'])
def read_item(item_id):
    item = items.get(item_id)
    
    if item is None:
        return jsonify({"error": "Item not found"}), 404
    
    return jsonify(item), 200

# Update Item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    name = data.get('name')

    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    items[item_id]['name'] = name
    return jsonify({"message": "Item updated successfully", "item": items[item_id]}), 200

# Delete Item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    if item_id not in items:
        return jsonify({"error": "Item not found"}), 404
    
    del items[item_id]
    return jsonify({"message": "Item deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
