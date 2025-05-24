from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_cors import CORS

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://samuelhoyosa:7712@cluster0.rtwsewy.mongodb.net/ferreteria?retryWrites=true&w=majority&appName=Cluster0"
mongo = PyMongo(app)
CORS(app)

def fix_id(document):
    document['_id'] = str(document['_id'])
    return document

@app.route('/api/users', methods=['GET'])
def get_users():
    users = list(mongo.db.users.find())
    return jsonify([fix_id(u) for u in users])

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    nuevo = {
        'nombre': data['nombre'],
        'empresa': data['empresa'],
        'cargo': data['cargo'],
        'telefono': data['telefono'],
        'correo': data['correo'],
        'contrasena': data['contrasena'],
        'verificacion': 1
    }
    result = mongo.db.users.insert_one(nuevo)
    return jsonify({'message': 'Usuario creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/users/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    mongo.db.users.update_one({'_id': ObjectId(id)}, {'$set': {
        'nombre': data['nombre'],
        'empresa': data['empresa'],
        'cargo': data['cargo'],
        'telefono': data['telefono'],
        'correo': data['correo'],
        'contrasena': data['contrasena']
    }})
    return jsonify({'message': 'Usuario actualizado'})

@app.route('/api/user_products', methods=['GET'])
def get_user_products():
    productos = list(mongo.db.user_products.find())
    return jsonify([fix_id(p) for p in productos])

@app.route('/api/user_products', methods=['POST'])
def create_user_product():
    data = request.get_json()
    nuevo = {
        'nombre_producto': data['nombre_producto'],
        'max_venta_diario': data['max_venta_diario'],
        'min_venta_diario': data['min_venta_diario'],
        'tiempo_provedor_despacho_dias': data['tiempo_provedor_despacho_dias'],
        'inventario_total': data['inventario_total'],
        'id_to_user': data['id_to_user']
    }
    result = mongo.db.user_products.insert_one(nuevo)
    return jsonify({'message': 'Producto creado', 'id': str(result.inserted_id)}), 201

@app.route('/api/user_products/<id>', methods=['PUT'])
def update_user_product(id):
    data = request.get_json()
    mongo.db.user_products.update_one({'_id': ObjectId(id)}, {'$set': {
        'nombre_producto': data['nombre_producto'],
        'max_venta_diario': data['max_venta_diario'],
        'min_venta_diario': data['min_venta_diario'],
        'tiempo_provedor_despacho_dias': data['tiempo_provedor_despacho_dias'],
        'inventario_total': data['inventario_total'],
        'id_to_user': data['id_to_user']
    }})
    return jsonify({'message': 'Producto actualizado'})

if __name__ == '__main__':
    app.run(debug=True)

